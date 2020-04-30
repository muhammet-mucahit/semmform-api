from django.urls import path
from form.views import FormList, FormDetail, FormfieldList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('forms/', FormList.as_view(), name="forms"),
    path('forms/<int:pk>/', FormDetail.as_view(), name="form-detail"),
    path('formfield/<int:pk>', FormfieldList.as_view(), name="formfield")
]

urlpatterns = format_suffix_patterns(urlpatterns)
