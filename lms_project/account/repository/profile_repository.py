from abc import ABC, abstractmethod


class ProfileRepository(ABC):
    @abstractmethod
    def findByEmail(self, email):
        pass

    @abstractmethod
    def create(self, email, password):
        pass

    @abstractmethod
    def decryption(self, email, password):
        pass