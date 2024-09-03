from abc import ABC, abstractmethod

class UserRecipeRepository(ABC):
    @abstractmethod
    def findLastRecipeByAccountId(self, accountId):
        pass

    @abstractmethod
    def save(self, userRecipeId):
        pass

    @abstractmethod
    def findByAccountIdAndRecipeId(self, accountId, userRecipeId):
        pass

    @abstractmethod
    def deleteByAccountIdAndRecipeId(self, accountId, userRecipeId):
        pass
