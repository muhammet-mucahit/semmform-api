from rest_framework import status
from account.models import User
from account.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


class UserDetail(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(user, data=request.data,
                                    partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
