from django.db import models


class AccountAttendanceCheck(models.Model):
    Attendance_cherry = models.IntegerField(default=0)
    Attendance_date1 = models.IntegerField(default=0)
    Attendance_date2 = models.IntegerField(default=0)
    Attendance_date3 = models.IntegerField(default=0)
    Attendance_date4 = models.IntegerField(default=0)
    Attendance_date5 = models.IntegerField(default=0)
    Attendance_date6 = models.IntegerField(default=0)
    Attendance_date7 = models.IntegerField(default=0)
    Attendance_date8 = models.IntegerField(default=0)
    Attendance_date9 = models.IntegerField(default=0)
    Attendance_date10 = models.IntegerField(default=0)
    Attendance_date11 = models.IntegerField(default=0)
    Attendance_date12 = models.IntegerField(default=0)
    Attendance_date13 = models.IntegerField(default=0)
    Attendance_date14 = models.IntegerField(default=0)
    Attendance_date15 = models.IntegerField(default=0)
    Attendance_date16 = models.IntegerField(default=0)
    Attendance_date17 = models.IntegerField(default=0)
    Attendance_date18 = models.IntegerField(default=0)
    Attendance_date19 = models.IntegerField(default=0)
    Attendance_date20 = models.IntegerField(default=0)
    Attendance_date21 = models.IntegerField(default=0)
    Attendance_date22 = models.IntegerField(default=0)
    Attendance_date23 = models.IntegerField(default=0)
    Attendance_date24 = models.IntegerField(default=0)
    Attendance_date25 = models.IntegerField(default=0)
    Attendance_date26 = models.IntegerField(default=0)
    Attendance_date27 = models.IntegerField(default=0)
    Attendance_date28 = models.IntegerField(default=0)
    Attendance_date29 = models.IntegerField(default=0)
    Attendance_date30 = models.IntegerField(default=0)
    Attendance_date31 = models.IntegerField(default=0)



    class Meta:
        db_table = 'account_attendance_check'
        app_label = 'account'