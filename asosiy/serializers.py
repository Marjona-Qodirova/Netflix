from rest_framework.exceptions import APIException
from rest_framework.serializers import ModelSerializer
from .models import *


class AktyorSerializer(ModelSerializer):
    class Meta:
        model = Aktyor
        fields = '__all__'
    def validate_jins(self, qiymat):
        jins=["Erkak", "Ayol", "Male", "Female"]
        if qiymat not in jins:
            raise APIException(" Malimotlar mos kelmadi")
        return qiymat



class KinoSerializer(ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'

    def validate_reyting(self, qiymat):

        if qiymat<4 :
            raise APIException(" Bunday reytingdagi kino yo'q!")
        return qiymat


