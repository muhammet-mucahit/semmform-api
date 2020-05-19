from django.db import models
from django.conf import settings
from form.enums import FormFieldType
import uuid


class FormField(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.TextField(null=False)
    is_required = models.BooleanField(default=False)
    type = models.CharField(
        max_length=100,
        choices=FormFieldType.choices,
        default=FormFieldType.SHORT_ANSWER,
    )

    def __str__(self):
        return f"{self.id} - {self.question} - {self.answer}"


class Form(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    answer_link_id = models.CharField(max_length=512, null=True)
    fields = models.ManyToManyField(FormField)

    def save(self, *args, **kwargs):
        self.answer_link_id = uuid.uuid1()
        super(Form, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description}"


class FormAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    answer = models.CharField(max_length=2000, null=False)
    # form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question = models.ForeignKey(FormField, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)