from attendance.repository.attendance_repository_impl import AttendanceRepositoryImpl
from attendance.service.attendance_service import AttendanceService


class AttendanceServiceImpl(AttendanceService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__attendanceRepository = AttendanceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def markAttendance(self):
        pass
    