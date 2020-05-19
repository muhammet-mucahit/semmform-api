from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/v1/', include('account.urls')),
    re_path('api/v1/', include('form.urls')),
]
