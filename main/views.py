from rest_framework import viewsets
from .models import *
from .serializers import *


class MenyuViewSet(viewsets.ModelViewSet):
    queryset = Menyu.objects.all()
    serializer_class = MenyuSerializer
    http_method_names = ['get']

class HomeViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomeSerializer
    http_method_names = ['get']


class SubMenyuViewSet(viewsets.ModelViewSet):
    queryset = SubMenyu.objects.all()
    serializer_class = SubMenyuSerializer
    http_method_names = ['get']


class MahsulotViewSet(viewsets.ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer
    http_method_names = ['get']

