from user_recipe.repository.user_recipe_repository_impl import UserRecipeRepositoryImpl
from user_recipe.service.user_recipe_service import UserRecipeService
from user_recipe.entity.user_recipe import UserRecipe

class UserRecipeServiceImpl(UserRecipeService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__repository = UserRecipeRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createUserRecipe(self, accountId):
        try:
            lastRecipe = self.__instance.__repository.findLastRecipeByAccountId(accountId)
            if lastRecipe:
                userRecipeId = lastRecipe.user_recipe_id + 1
            else:
                userRecipeId = 1

            print(f"Generated userRecipeId: {userRecipeId} for accountId: {accountId}")

            userRecipeIdInstance = UserRecipe(account_id=accountId, user_recipe_id=userRecipeId)
            return self.__instance.__repository.save(userRecipeIdInstance)
        except Exception as e:
            print(f"Error in createUserRecipe: {str(e)}")
            raise

    def getUserRecipe(self, accountId, userRecipeId):
        return self.__repository.findByAccountIdAndRecipeId(accountId, userRecipeId)

    def deleteUserRecipe(self, accountId, userRecipeId):
        return self.__repository.deleteByAccountIdAndRecipeId(accountId, userRecipeId)
