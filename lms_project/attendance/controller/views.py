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
            current_month = request.data.get('month')
            print(f"current_month: {current_month}")
            accountInfo = self.redisService.getValueByKey(user_token)
            account_id = accountInfo['account_id']
            accountMonthInfo = self.accountService.findAttendance_DateByAccountId(account_id)
            print(f"user's_month: {accountMonthInfo}")

            if current_month != accountMonthInfo:
                print("초기화 로직 진입 성공")
                self.accountService.setNewMonth(account_id, current_month)
                self.redisService.reinit_double_key_value(account_id)

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

            self.redisService.store_double_key_value(accountId, day)

            attendanceCherry = self.accountService.findAttendance_CherryByAccountId(accountId)
            print(f"attendance cherry: {attendanceCherry}")
            attendanceCherry += 50

            self.accountService.updateAttendanceCherry(accountId, attendanceCherry)
            return Response({'attendanceDateList': attendanceCherry}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error get user's Attendance:{e}")
            return False, str(e)
