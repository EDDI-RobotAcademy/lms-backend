from abc import ABC, abstractmethod


class AttendanceService(ABC):
    @abstractmethod
    def findTodayForAttendance(self):
        pass
