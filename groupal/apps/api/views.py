from django.shortcuts import render
from rest_framework import generics
from serializers import TestModelSerializer
from groupal.apps.data.models import TestModel

# Create your views here.

class TestList(generics.ListCreateAPIView):
    serializer_class = TestModelSerializer
    queryset = TestModel.objects.all()


class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TestModelSerializer
    queryset = TestModel.objects.all()