from user_recipe.entity.user_recipe import UserRecipe
from user_recipe.repository.user_recipe_repository import UserRecipeRepository

class UserRecipeRepositoryImpl(UserRecipeRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def findLastRecipeByAccountId(self, accountId):
        try:
            lastRecipe = UserRecipe.objects.filter(account_id=accountId).order_by('-recipe_hash').first()  # recipe_hash 사용
            print(f"Last recipe for accountId {accountId}: {lastRecipe}")
            return lastRecipe
        except Exception as e:
            print(f"Error in findLastRecipeByAccountId: {str(e)}")
            raise

    def save(self, userRecipe):
        user_recipe_obj = UserRecipe(account_id=userRecipe['account_id'], recipe_hash=userRecipe['recipe_hash'])
        user_recipe_obj.save()  # UserRecipe 객체 저장
        return user_recipe_obj

    def findByAccountIdAndRecipeHash(self, accountId, recipeHash):
        return UserRecipe.objects.filter(account_id=accountId, recipe_hash=recipeHash).first()

    def deleteByAccountIdAndRecipeHash(self, accountId, recipeHash):  # recipeHash로 삭제
        return UserRecipe.objects.filter(account_id=accountId, recipe_hash=recipeHash).delete()
