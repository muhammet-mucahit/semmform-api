from django.urls import path
from account.views import UserDetail

urlpatterns = [
    path('users/<username>/', UserDetail.as_view(), name="user-detail")
]
