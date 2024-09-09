from user_recipe.repository.user_recipe_repository_impl import UserRecipeRepositoryImpl
from user_recipe.service.user_recipe_service import UserRecipeService


class UserRecipeServiceImpl(UserRecipeService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__userRecipeRepository = UserRecipeRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createUserRecipe(self, account_id: int, recipe_hash: str):

        # 중복 확인
        existing_recipe = self.__userRecipeRepository.checkDuplicationHashedRecipe(account_id, recipe_hash)
        if existing_recipe:
            print(f"Recipe already exists for account_id {account_id} and recipe_hash {recipe_hash}")
            return None  # 중복된 레시피가 있으면 저장하지 않음

        # 새로운 레시피 저장
        new_recipe = self.__userRecipeRepository.save({
            "account_id": account_id,
            "recipe_hash": recipe_hash
        })
        return new_recipe

    def getHashedRecipeByAccountId(self, account_id):
        return self.__userRecipeRepository.findHashedRecipeByAccountId(account_id)

    # TODO. mongoDB에서 가져오는 함수 구현하기
    def getRecipeFromMongDB(self, account_id, recipe_hash):
        return self.__userRecipeRepository.findRecipeFromMongoDB(account_id, recipe_hash)

    def deleteUserRecipeByAccountIdAndRecipeHash(self, account_id: int, recipe_hash: str):
        return self.__userRecipeRepository.deleteByAccountIdAndRecipeHash(account_id, recipe_hash)
