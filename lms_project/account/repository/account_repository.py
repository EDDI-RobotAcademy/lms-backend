from abc import ABC, abstractmethod


class AccountRepository(ABC):
    @abstractmethod
    def create(self, paidmemberType, loginType):
        pass

    @abstractmethod
    def findPaidMemberType(self, accountId):
        pass