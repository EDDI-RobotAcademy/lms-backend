from abc import ABC, abstractmethod


class ProfileRepository(ABC):
    @abstractmethod
    def findByEmail(self, email):
        pass

    @abstractmethod
    def create(self, email, password, account):
        pass

    @abstractmethod
    def createSocial(self, email, account):
        pass

    @abstractmethod
    def decryption(self, email, password):
        pass

    @abstractmethod
    def findByLoginType(self, email):
        pass

    @abstractmethod
    def findByAccount(self, accountId):
        pass