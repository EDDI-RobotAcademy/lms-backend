from account.entity.account import Account
from account.entity.account_login_type import AccountLoginType
from account.entity.account_paid_member_type import AccountPaidMemberType
from account.entity.profile import Profile
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

    def create(self, paidmemberType, loginType):
        loginTypeEntity = AccountLoginType.objects.create(loginType=loginType)

        paidmemberTypeEntity = AccountPaidMemberType.objects.create(paidmemberType=paidmemberType)

        account = Account.objects.create(
            loginType=loginTypeEntity,
            paidmemberType=paidmemberTypeEntity
        )

        return account