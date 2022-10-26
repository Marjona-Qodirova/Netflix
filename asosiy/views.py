from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *

#
# class HammaAktyorlarAPI(APIView):
#     def get(self, request):
#         aktyorlar=Aktyor.objects.all()
#         ser=AktyorSerializer(aktyorlar, many=True)
#         return  Response(ser.data)
#
#     def post(self, request):
#         aktyor = request.data
#         ser = AktyorSerializer(data=aktyor)
#         if ser.is_valid():
#             ser.save()
#             return Response({"xabar": "Ma'lumot qo'shildi", "malumot": ser.data})
#         return Response({"xabar": "Ma'lumot qo'shilmadi. Xatolik bor"})
# class AktyorAPI(APIView):
#     def get(self, request, pk):
#         aktyor=Aktyor.objects.get(id=pk)
#         ser=AktyorSerializer(aktyor)
#         return Response(ser.data)
#
#     def put(self, request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         ser = AktyorSerializer(aktyor, request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response({"xabar": "Ma'lumot o'zgardi", "malumot": ser.data})
#         return Response({"xabar": "Ma'lumot o'zgarmadi. Xatolik bor"})
#
#     def delete(self, request, pk):
#         Aktyor.objects.get(id=pk).delete()
#         return Response({"xabar": "Ma'lumot ochirildi"})
#
#
# class HammaKinolarAPI(APIView):
#     def get(self, request):
#         kinolar = Kino.objects.all()
#         ser = KinoSerializer(kinolar, many=True)
#         return Response(ser.data)
#     def post(self, request):
#         kino=request.data
#         ser=KinoSerializer(data=kino)
#         if ser.is_valid():
#             ser.save()
#             return Response({"xabar": "Ma'lumot qoshildi", "malumot":ser.data})
#         return Response({"xabar":"Ma'lumot qoshilmadi. Xatolik bor"})
# class KinoAPI(APIView):
#     def get(self, request, pk):
#         kino=Kino.objects.get(id=pk)
#         ser=KinoSerializer(kino)
#         return Response(ser.data)
#
#     def put(self, request, pk):
#         kino = Kino.objects.get(id=pk)
#         ser = KinoSerializer(kino, request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response({"xabar": "Ma'lumot o'zgardi", "malumot": ser.data})
#         return Response({"xabar": "Ma'lumot o'zgarmadi. Xatolik bor"})
#
#     def delete(self, request, pk):
#         Kino.objects.get(id=pk).delete()
#         return Response({"xabar": "Ma'lumot ochirildi"})
#
#
class AktyorViewSet(ModelViewSet):
    queryset = Aktyor.objects.all()
    serializer_class = AktyorSerializer
    permission_classes = [IsAuthenticated, ]

    @action(methods=['GET'], detail=True)
    def kinolar(self, request, pk):
        aktyor=Aktyor.objects.get(id=pk)
        films=Kino.objects.filter(aktyorlar=aktyor)
        ser = KinoSerializer(films, many=True)
        return Response(ser.data)


class KinoViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer
    permission_classes = [IsAuthenticated, ]
    @action(methods=['GET'], detail=True)
    def aktyorlar(self, request, pk):
        kino=Kino.objects.get(id=pk)
        actors=kino.aktyorlar
        ser=AktyorSerializer(actors, many=True)
        return  Response(ser.data)



class HammaKinolar(ListCreateAPIView):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer


class KinoGetDeleteUpdete(RetrieveUpdateDestroyAPIView):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer




class HammaAktyorlar(ListCreateAPIView):
    queryset = Aktyor.objects.all()
    serializer_class = AktyorSerializer

class AktyorGetDeleteUpdete(RetrieveUpdateDestroyAPIView):
    queryset = Aktyor.objects.all()
    serializer_class = AktyorSerializer




