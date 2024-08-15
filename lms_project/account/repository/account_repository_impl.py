from account.entity.account import Account
from account.entity.account_login_type import AccountLoginType
from account.repository.account_repository import AccountRepository

class AccountRepositoryImpl(AccountRepository):
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

    def create(self, loginType):
        loginTypeEntity = AccountLoginType.objects.create(loginType=loginType)

        account = Account.objects.create(loginType=loginTypeEntity)
        return account
