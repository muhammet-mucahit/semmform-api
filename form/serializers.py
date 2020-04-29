from rest_framework import serializers
from form.models import Form


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
