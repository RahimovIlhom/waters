from rest_framework import serializers
from .models import *


class MenyuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menyu
        fields = '__all__'

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'

    def to_representation(self, instance):
        menyu = super().to_representation(instance)
        menyu['submenyular'] = SubMenyuSerializer(SubMenyu.objects.filter(menyu=instance), many=True).data
        return menyu


class SubMenyuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenyu
        fields = '__all__'

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model= Mahsulot
        fields='__all__'