# Generated by Django 3.0.5 on 2020-05-17 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_formanswer_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formfield',
            name='description',
        ),
    ]
