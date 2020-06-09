from form.models import Form, FormField, FormAnswer
from form.serializers import FormSerializer, FormFieldSerializer, \
    FormFieldBulkSerializer, FormAnswerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from account.models import User
from rest_framework.decorators import api_view


class FormList(APIView):
    """
    List all snippets, or create a new form.
    """

    def get(self, request):
        forms = Form.objects.filter(user=request.user)
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            form = serializer.save()
            user = User.objects.filter(username=request.user).first()
            user.forms.add(form)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormDetail(APIView):
    """
    Retrieve, update or delete a form instance.
    """

    def get_object(self, pk):
        try:
            return Form.objects.get(user=self.request.user, pk=pk)
        except Form.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        form = self.get_object(pk)
        serializer = FormSerializer(form)
        return Response(serializer.data)

    def patch(self, request, pk):
        form = self.get_object(pk)
        serializer = FormSerializer(form, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        form = self.get_object(pk)
        form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FormAnswers(APIView):
    def get_object(self, link):
        try:
            return Form.objects.get(answer_link_id=link)
        except Form.DoesNotExist:
            raise Http404

    def get(self, request, link):
        form = self.get_object(link)
        serializer = FormSerializer(form)
        return Response(serializer.data)


class FormFieldList(APIView):
    def get_object(self, pk):
        try:
            return Form.objects.get(user=self.request.user, pk=pk)
        except Form.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        form = self.get_object(pk)
        fields = form.fields.all()
        serializer = FormFieldSerializer(fields, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        form = self.get_object(pk)
        serializer = FormFieldSerializer(data=request.data)
        if serializer.is_valid():
            form_field = serializer.save()
            form.fields.add(form_field)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormFieldDetail(APIView):
    # def get(self, request, form_id, field_id):
    #     form = Form.objects.get(pk=form_id)
    #     formfields = form.fields.all()
    #     serializer = FormFieldSerializer(formfields, many=True)
    #     return Response(serializer.data)

    def delete(self, request, pk):
        form_field = FormField.objects.get(pk=pk)
        form_field.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FormFieldBulkAdd(APIView):
    def get_object(self, pk):
        try:
            return Form.objects.get(user=self.request.user, pk=pk)
        except Form.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        form = self.get_object(pk)
        serializer = FormFieldBulkSerializer(data=request.data)
        if serializer.is_valid():
            form_fields = serializer.save()
            for field in form_fields:
                field.save()
                form.fields.add(field)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FormAnswerView(APIView):
    def get_object(self, link):
        try:
            form = Form.objects.get(user=self.request.user, answer_link_id=link)
            return form
        except Form.DoesNotExist:
            raise Http404

    def get(self, request, link):
        form = self.get_object(link)
        answers = FormAnswer.objects.filter(question__form__id=form.id)
        serializer = FormAnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request, link):
        data = request.data
        for key, value in data.items():
            question_id = key
            answer = FormAnswer()
            answer.answer = value
            answer.question_id = question_id
            answer.user = request.user
            answer.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def new_form(request):
    if request.method == 'POST':
        form = None
        form_serializer = FormSerializer(data=request.data)
        if form_serializer.is_valid():
            form = form_serializer.save()
            user = User.objects.filter(username=request.user).first()
            user.forms.add(form)

        fields = request.data.get('fields', [])
        for field in fields:
            serializer = FormFieldSerializer(data=field)
            if serializer.is_valid():
                form_field = serializer.save()
                form.fields.add(form_field)

        return Response(form_serializer.data, status=status.HTTP_200_OK)
    return Response({"forms": FormAnswer.objects.all()},
                    status=status.HTTP_200_OK)
