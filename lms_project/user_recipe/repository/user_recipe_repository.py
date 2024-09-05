from abc import ABC, abstractmethod

class UserRecipeRepository(ABC):
    @abstractmethod
    def findLastRecipeByAccountId(self, accountId):
        pass

    @abstractmethod
    def save(self, userRecipe):
        pass

    @abstractmethod
    def findByAccountIdAndRecipeHash(self, accountId, recipeHash):  # recipeHash로 조회
        pass

    @abstractmethod
    def deleteByAccountIdAndRecipeHash(self, accountId, recipeHash):  # recipeHash로 삭제
        pass
