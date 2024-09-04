from abc import ABC, abstractmethod


class AttendanceRepository(ABC):
    @abstractmethod
    def mark(self):
        pass
