from abc import ABC, abstractmethod


class UserRecipeService(ABC):

    @abstractmethod
    def createUserRecipe(self, account_id: int, recipe_hash: str):
        pass

    @abstractmethod
    def getUserRecipeByAccountIdAndRecipeHash(self, account_id: int, recipe_hash: str):
        pass

    @abstractmethod
    def deleteUserRecipeByAccountIdAndRecipeHash(self, account_id: int, recipe_hash: str):
        pass
