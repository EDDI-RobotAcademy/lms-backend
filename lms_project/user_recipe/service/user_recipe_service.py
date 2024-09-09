from abc import ABC, abstractmethod


class UserRecipeService(ABC):

    @abstractmethod
    def createUserRecipe(self, account_id, recipe_hash):
        pass

    @abstractmethod
    def getHashedRecipeByAccountId(self, account_id):
        pass

    @abstractmethod
    def getRecipeFromMongDB(self, account_id, recipe_hash):
        pass

    @abstractmethod
    def deleteUserRecipeByAccountIdAndRecipeHash(self, account_id, recipe_hash):
        pass
