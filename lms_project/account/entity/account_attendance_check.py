from django.db import models


class AccountAttendanceCheck(models.Model):
    Attendance_cherry = models.IntegerField(default=0)
    Attendance_date = models.IntegerField(default=0)



    class Meta:
        db_table = 'account_attendance_check'
        app_label = 'account'