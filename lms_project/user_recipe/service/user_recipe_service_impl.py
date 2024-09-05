from user_recipe.repository.user_recipe_repository_impl import UserRecipeRepositoryImpl
from user_recipe.service.user_recipe_service import UserRecipeService


class UserRecipeServiceImpl(UserRecipeService):
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

    def createUserRecipe(self, account_id: int, recipe_hash: str):
        repository = UserRecipeRepositoryImpl.getInstance()

        # 중복 확인
        existing_recipe = repository.findByAccountIdAndRecipeHash(account_id, recipe_hash)
        if existing_recipe:
            print(f"Recipe already exists for account_id {account_id} and recipe_hash {recipe_hash}")
            return None  # 중복된 레시피가 있으면 저장하지 않음

        # 새로운 레시피 저장
        new_recipe = repository.save({
            "account_id": account_id,
            "recipe_hash": recipe_hash
        })
        return new_recipe

    def getUserRecipeByAccountIdAndRecipeHash(self, account_id: int, recipe_hash: str):
        repository = UserRecipeRepositoryImpl.getInstance()
        return repository.findByAccountIdAndRecipeHash(account_id, recipe_hash)

    def deleteUserRecipeByAccountIdAndRecipeHash(self, account_id: int, recipe_hash: str):
        repository = UserRecipeRepositoryImpl.getInstance()
        return repository.deleteByAccountIdAndRecipeHash(account_id, recipe_hash)
