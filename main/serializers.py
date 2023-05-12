from rest_framework import serializers
from .models import *


class MenyuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menyu
        fields = '__all__'

    def to_representation(self, instance):
        menyu = super().to_representation(instance)
        menyu['submenyular'] = SubMenyuSerializer(SubMenyu.objects.filter(menyu=instance), many=True).data
        return menyu

class UlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ul
        fields = '__all__'

    def to_representation(self, instance):
        ul = super().to_representation(instance)
        ul['list'] = ListSerializer(List.objects.filter(ul=instance), many=True).data
        return ul


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'


class SubMenyuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenyu
        fields = '__all__'

    def to_representation(self, instance):
        submenyu = super().to_representation(instance)
        submenyu['ul'] = UlSerializer(Ul.objects.filter(submenyu=instance), many=True).data
        return submenyu

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model= Mahsulot
        fields='__all__'