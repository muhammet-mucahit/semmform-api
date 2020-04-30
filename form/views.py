from form.models import Form, FormField
from form.serializers import FormSerializer, FormFieldSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from account.models import User


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


class FormfieldList(APIView):

    def get(self, request, pk):
        form = Form.objects.get(pk=pk)
        formfields = form.fields.all()
        serializer = FormFieldSerializer(formfields, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormFieldSerializer(data=request.data)
        if serializer.is_valid():
            form = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
