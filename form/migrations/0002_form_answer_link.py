# Generated by Django 3.0.5 on 2020-05-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='answer_link',
            field=models.URLField(null=True),
        ),
    ]
