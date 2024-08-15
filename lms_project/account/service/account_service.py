from abc import ABC, abstractmethod


class AccountService(ABC):

    @abstractmethod
    def checkEmailDuplication(self, email):
        pass

    @abstractmethod
    def registerAccount(self,loginType, email, password):
        pass

    @abstractmethod
    def registerSocialAccount(self, loginType, email):
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