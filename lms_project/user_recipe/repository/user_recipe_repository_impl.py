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
            lastRecipe = UserRecipe.objects.filter(account_id=accountId).order_by('-user_recipe_id').first()
            print(f"Last recipe for accountId {accountId}: {lastRecipe}")
            return lastRecipe
        except Exception as e:
            print(f"Error in findLastRecipeByAccountId: {str(e)}")
            raise

    def save(self, userRecipeId):
        userRecipeId.save()  # UserRecipeId 객체 저장
        return userRecipeId

    def findByAccountIdAndRecipeId(self, accountId, userRecipeId):
        return UserRecipe.objects.get(account_id=accountId, user_recipe_id=userRecipeId)

    def deleteByAccountIdAndRecipeId(self, accountId, userRecipeId):
        return UserRecipe.objects.filter(account_id=accountId, user_recipe_id=userRecipeId).delete()
