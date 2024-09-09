from abc import ABC, abstractmethod

class UserRecipeRepository(ABC):
    @abstractmethod
    def findLastRecipeByAccountId(self, accountId):
        pass

    @abstractmethod
    def save(self, userRecipe):
        pass

    @abstractmethod
    def checkDuplicationHashedRecipe(self, account_id, recipe_hash):
        pass

    @abstractmethod
    def findHashedRecipeByAccountId(self, accountId):
        pass

    @abstractmethod
    def findRecipeFromMongoDB(self, account_id, recipe_hash):
        pass

    @abstractmethod
    def deleteByAccountIdAndRecipeHash(self, accountId, recipeHash):  # recipeHash로 삭제
        pass
