from abc import ABC, abstractmethod


class AttendanceService(ABC):
    @abstractmethod
    def markAttendance(self):
        pass
