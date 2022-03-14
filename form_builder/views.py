from django.shortcuts import render
from rest_framework import viewsets

from .models import Api
from .serializers import ApiSerializer
# Create your views here.

class ApiView(viewsets.ModelViewSet):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer