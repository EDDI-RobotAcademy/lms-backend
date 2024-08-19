from abc import ABC, abstractmethod


class AccountRepository(ABC):
    @abstractmethod
    def create(self, Ticket, paidmemberType, loginType):
        pass

    @abstractmethod
    def findPaidMemberType(self, accountId):
        pass

    @abstractmethod
    def findTicket(self, accountId):
        pass