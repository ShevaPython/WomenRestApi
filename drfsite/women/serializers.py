import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'content', 'cat')

# class CreateWomenModel:
#     '''Создания тест модели для работы с json and serializatir'''
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class WomenSerializer(serializers.Serializer):
#     '''Сериализатор класс Women от базового класса Serializer'''
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_publish = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         '''Создания обьэкта в базу данных'''
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         '''Обновления обьэкта в базу даных'''
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_create = validated_data.get('time_create', instance.time_create)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_publish = validated_data.get('is_publish', instance.is_publish)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance
#


# def encode():
#     '''Кодирование в json-data'''
#     model = CreateWomenModel('Victoria', 'Content :Shevtsova')
#     model_finish = WomenSerializer(model)
#     print(model_finish.data, type(model_finish.data), sep='\n')
#     json = JSONRenderer().render(model_finish.data)
#     print(json)

# #
# # def decode():
#        """Декодирования с json"""
# #     stream = io.BytesIO(b'{"title":"Victoria","content":"Content :Shevtsova"}')
# #     data = JSONParser().parse(stream)
# #     serializer = WomenSerializer(data=data)
# #     serializer.is_valid()
# #     print(serializer.validated_data)
