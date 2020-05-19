from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'is_superuser', 'user_permissions', 'groups', 'last_login',
            'password', 'is_staff', 'is_active', 'forms')
        # depth = 2
