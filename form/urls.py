from django.urls import path
from form.views import FormList, FormDetail, FormFieldDetail, FormFieldList, \
    FormFieldBulkAdd, FormAnswers, FormAnswerView, new_form
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('forms/', FormList.as_view(), name="forms"),
    path('forms/<int:pk>/', FormDetail.as_view(), name="form-detail"),
    path('forms/answers/<str:link>/', FormAnswers.as_view()),
    path('forms/answers/answer/<str:link>/', FormAnswerView.as_view()),
    path('forms/<int:pk>/formfields/', FormFieldList.as_view()),
    path('forms/<int:pk>/formfields/bulk', FormFieldBulkAdd.as_view(), name="bulk_add"),
    path('formfields/<int:pk>', FormFieldDetail.as_view(), name="formfield"),
    path('new_form/', new_form)
]

urlpatterns = format_suffix_patterns(urlpatterns)
