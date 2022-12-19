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
        return Response({'post': WomenSerializer(womenlist,many=True).data})

    def post(self, request):
        serializator = WomenSerializer(data=request.data)
        serializator.is_valid(raise_exception=True)
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': WomenSerializer(post_new).data})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
