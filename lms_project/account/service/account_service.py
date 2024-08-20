from abc import ABC, abstractmethod


class AccountService(ABC):

    @abstractmethod
    def checkEmailDuplication(self, email):
        pass

    @abstractmethod
    def registerAccount(self, Cherry,Ticket, paidmemberType, loginType, email, password, nickname):
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
    def findEmailByAccountId(self, accountId):
        pass

    @abstractmethod
    def findPaidMemberTypeByAccountId(self, accountId):
        pass

    @abstractmethod
    def findTicketByAccountId(self, accountId):
        pass

    @abstractmethod
    def checkNickNameDuplication(self, nickname):
        pass

    @abstractmethod
    def updateTicketCount(self, user_id, new_ticket_count):
        pass

    @abstractmethod
    def findNicknameByAccountId(self, accountId):
        pass