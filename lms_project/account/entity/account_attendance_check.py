from django.db import models


class AccountAttendanceCheck(models.Model):
    Attendance_cherry = models.IntegerField(default=0)
    Attendance_monthly_check = models.IntegerField(default=0)
    Attendance_last_login_month = models.IntegerField(default=0)

    class Meta:
        db_table = 'account_attendance_check'
        app_label = 'account'
