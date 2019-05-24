from django.shortcuts import render
from django.http import HttpResponse
from .models import Bars
from rest_framework import viewsets
from .serializers import BarsSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")
# Create your views here.
class BarsViewSet(viewsets.ModelViewSet):
    queryset = Bars.objects.all().order_by('-datetime')
    serializer_class = BarsSerializer
