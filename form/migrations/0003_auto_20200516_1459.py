# Generated by Django 3.0.5 on 2020-05-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_form_answer_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='answer_link',
            field=models.URLField(null=True, unique=True),
        ),
    ]