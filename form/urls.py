from django.urls import path
from form.views import FormList, FormDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('forms/', FormList.as_view(), name="forms"),
    path('forms/<int:pk>/', FormDetail.as_view(), name="form-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
