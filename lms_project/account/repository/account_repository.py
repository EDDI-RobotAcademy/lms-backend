from abc import ABC, abstractmethod


class AccountRepository(ABC):
    @abstractmethod
    def create(self, Attendance_date, Attendance_cherry, Cherry, Ticket, paidmemberType, loginType):
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

    @abstractmethod
    def findCherry(self, accountId):
        pass

    @abstractmethod
    def findAttendance_Cherry(self, accountId):
        pass

    @abstractmethod
    def findAttendance_Date(self, accountId):
        pass

    @abstractmethod
    def updateCherry(self, user_id, new_cherry_count):
        pass

    @abstractmethod
    def updateAttendanceCherry(self, account_id, new_attendanceCherry):
        pass

    @abstractmethod
    def setNewMonth(self, account_id, account_month_info):
        pass