from abc import ABC, abstractmethod

class UserRecipeService(ABC):

    @abstractmethod
    def createUserRecipe(self, accountId):
        pass

    @abstractmethod
    def getUserRecipe(self, accountId, userRecipeId):
        pass

    @abstractmethod
    def deleteUserRecipe(self, accountId, userRecipeId):
        pass
