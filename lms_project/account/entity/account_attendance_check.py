from django.db import models


class AccountAttendanceCheck(models.Model):
    Attendance_cherry = models.IntegerField(default=0)
    Monthly_attendance_flag = models.BooleanField(default=False)



    class Meta:
        db_table = 'account_attendance_check'
        app_label = 'account'