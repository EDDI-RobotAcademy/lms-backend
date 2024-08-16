from abc import ABC, abstractmethod


class AccountService(ABC):

    @abstractmethod
    def checkEmailDuplication(self, email):
        pass

    @abstractmethod
    def registerAccount(self, paidmemberType, loginType, email, password):
        pass

    @abstractmethod
    def registerSocialAccount(self, paidmemberType, loginType, email):
        pass

    @abstractmethod
    def decryptionPassword(self, email, password):
        pass

    @abstractmethod
    def checkLoginType(self, email):
        pass

    @abstractmethod
    def findAccountByEmail(self, email):
        pass

    @abstractmethod
    def checkPaidMemberType(self, email):
        pass

    @abstractmethod
    def findEmailByAccountId(self, accountId):
        pass

    @abstractmethod
    def findPaidMemberTypeByAccountId(self, accountId):
        pass