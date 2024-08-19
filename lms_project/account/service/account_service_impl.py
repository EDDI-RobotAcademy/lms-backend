from account.repository.account_repository_impl import AccountRepositoryImpl
from account.repository.profile_repository_impl import ProfileRepositoryImpl
from account.service.account_service import AccountService

class AccountServiceImpl(AccountService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__profileRepository = ProfileRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def checkEmailDuplication(self, email):
        profile = self.__profileRepository.findByEmail(email)
        return profile is not None

    def registerAccount(self, paidmemberType, loginType, email, password):
        account = self.__accountRepository.create(paidmemberType, loginType)
        return self.__profileRepository.create(email, password, account)

    def registerSocialAccount(self, paidmemberType, loginType, email):
        account = self.__accountRepository.create(paidmemberType, loginType)
        return self.__profileRepository.createSocial(email, account)

    def decryptionPassword(self, email, password):
        return self.__profileRepository.decryption(email, password)

    def checkLoginType(self, email):
        loginType = self.__profileRepository.findByLoginType(email)
        return loginType

    def findAccountByEmail(self, email):
        profile = self.__profileRepository.findByEmail(email)

        return profile

    def findEmailByAccountId(self, accountId):
        email = self.__profileRepository.findByAccount(accountId)
        return email

    def findPaidMemberTypeByAccountId(self, accountId):
        paidmembertype = self.__accountRepository.findPaidMemberType(accountId)
        return paidmembertype
