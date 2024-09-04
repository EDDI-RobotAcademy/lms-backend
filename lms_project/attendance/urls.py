from django.urls import path, include
from rest_framework.routers import DefaultRouter
from attendance.controller.views import AttendanceView

router = DefaultRouter()
router.register(r'', AttendanceView, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
    path('attendance-list',
         AttendanceView.as_view({'post': 'attendanceList'}),
         name='attendanceList'),
    path('mark-attendance',
         AttendanceView.as_view({'post': 'markAttendance'}),
         name='markAttendance'),
]
