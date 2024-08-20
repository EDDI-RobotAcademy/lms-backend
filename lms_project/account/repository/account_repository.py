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

    @abstractmethod
    def updateTicket(self, user_id, new_ticket_count):
        pass