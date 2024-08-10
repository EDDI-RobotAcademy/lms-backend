from rest_framework import serializers

from account.entity.profile import Profile


# 실제 사용할 데이터의 형식이 무엇인지를 알려줍니다
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['email', 'password']
