from django.db import models
from form.enums import FormFieldType


class FormField(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.TextField(null=False)
    answer = models.TextField(null=True)
    description = models.TextField(null=True)
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
    fields = models.ManyToManyField(FormField)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description}"
