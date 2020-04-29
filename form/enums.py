# from enum import Enum
from django.db import models


class FormFieldType(models.TextChoices):
    SHORT_ANSWER = 'Short Answer'
    PARAGRAPH = 'Paragraph'
