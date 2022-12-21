from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response

from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework.views import APIView


class WomenAPIView(APIView):
    def get(self, request):
        womenlist = Women.objects.all()
        return Response({'post': WomenSerializer(womenlist, many=True).data})

    def post(self, request):
        '''Сохранения в базу даных'''
        serializator = WomenSerializer(data=request.data)
        serializator.is_valid(raise_exception=True)
        serializator.save()

        return Response({'post': serializator.data})

    def put(self, request, *args, **kwargs):
        '''Обновления записей в базе даных'''
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Method put not allowed"})
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': "Object does not exist"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        '''Удаления из базы дааных'''
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Method delete not allowed"})
        try:
            record = Women.objects.filter(pk=pk)
            record.delete()
        except:
            return Response({'error': "Object does not exist"})

        return Response({"post": "delete post " + str(pk)})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
