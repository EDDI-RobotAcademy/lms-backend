from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from attendance.service.attendance_service_impl import AttendanceServiceImpl
# ??????? google_oauth ???????
from google_oauth.service.redis_service_impl import RedisServiceImpl


# Create your views here.
class AttendanceView(viewsets.ViewSet):
    attendanceService = AttendanceServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def attendanceList(self, request):
        try:
            user_token = request.data.get('usertoken')
            accountInfo = self.redisService.getValueByKey(user_token)
            account_id = accountInfo['account_id']

            self.attendanceService.findTodayForAttendance()

            self.redisService.store_double_key_value(account_id, 18, True)
            attendanceList = self.redisService.double_key_value_list(account_id)
            print(f"attendance list: {attendanceList}")

            return Response({'attendanceDateList': attendanceList}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error get user's Attendance:{e}")
            return False, str(e)