from rest_framework import serializers
from form.models import Form, FormField, FormAnswer


class FormAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAnswer
        fields = '__all__'


class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = '__all__'


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
        depth = 1


class FormFieldBulkSerializer(serializers.ListSerializer):
    child = FormFieldSerializer()

    def update(self, instance, validated_data):
        form_fields = [FormField(**item) for item in validated_data]
        print(form_fields)
        for field in form_fields:
            if field.id:
                form_fields.remove(field)
        print(form_fields)
        return FormField.objects.bulk_create(form_fields)

    def create(self, validated_data):
        form_fields = [FormField(**item) for item in validated_data]
        print(form_fields)
        for field in form_fields:
            if field.id:
                form_fields.remove(field)
        print(form_fields)
        return FormField.objects.bulk_create(form_fields)
