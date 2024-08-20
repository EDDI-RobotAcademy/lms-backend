from account.entity.account import Account
from account.entity.account_login_type import AccountLoginType
from account.entity.account_paid_member_type import AccountPaidMemberType
from account.entity.account_ticket import AccountTicket
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

    def create(self, Ticket, paidmemberType, loginType):
        loginTypeEntity = AccountLoginType.objects.create(loginType=loginType)

        paidmemberTypeEntity = AccountPaidMemberType.objects.create(paidmemberType=paidmemberType)

        ticketEntity = AccountTicket.objects.create(Ticket=Ticket)

        account = Account.objects.create(
            loginType=loginTypeEntity,
            paidmemberType=paidmemberTypeEntity,
            Ticket=ticketEntity
        )

        return account

    def findPaidMemberType(self, accountId):
        account = AccountPaidMemberType.objects.get(id=accountId)
        paidmemberType = AccountPaidMemberType.objects.get(paidmemberType=account.paidmemberType)
        print("findPaidMemberType 출력", paidmemberType.paidmemberType)
        return paidmemberType.paidmemberType

    def findTicket(self, accountId):
        account = AccountTicket.objects.get(id=accountId)
        print("findTicket 출력", account.Ticket)
        if account.Ticket:
            return account.Ticket  # 대문자 T를 사용


    def updateTicket(self, user_id, new_ticket_count):
        try:
            account = Account.objects.get(id=user_id)
            ticket = account.Ticket
            ticket.Ticket = new_ticket_count
            ticket.save()
            return True
        except Exception as e:
            print(f"Error updating ticket count: {e}")
            return False
