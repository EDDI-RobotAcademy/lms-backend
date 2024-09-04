from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from attendance.service.attendance_service_impl import AttendanceServiceImpl
# ??????? google_oauth ???????
from google_oauth.service.redis_service_impl import RedisServiceImpl


# Create your views here.
class AttendanceView(viewsets.ViewSet):
    attendanceService = AttendanceServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()

    def attendanceList(self, request):
        try:
            user_token = request.data.get('usertoken')
            accountInfo = self.redisService.getValueByKey(user_token)
            account_id = accountInfo['account_id']

            attendanceList = self.redisService.double_key_value_list(account_id)
            print(f"attendance list: {attendanceList}")

            return Response({'attendanceDateList': attendanceList}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error get user's Attendance:{e}")
            return False, str(e)

    def markAttendance(self, request):
        try:
            print(f"request: {request}")
            user_token = request.data.get('usertoken')
            day = request.data.get('today')
            print(f"day: {day}")
            accountInfo = self.redisService.getValueByKey(user_token)
            accountId = accountInfo['account_id']

            attendanceCherry = self.accountService.findCherryByAccountId(accountId)
            print(f"attendance cherry: {attendanceCherry}")
            attendanceCherry += 50

            self.accountService.updateAttendanceCherry(accountId, attendanceCherry)
            return Response({'attendanceDateList': attendanceCherry}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error get user's Attendance:{e}")
            return False, str(e)
