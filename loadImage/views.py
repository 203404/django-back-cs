# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

import os.path

# Imports from models and serializers
from loadImage.models import LoadImage
from loadImage.serializers import LoadImageSerializers

class LoadImageTable(APIView):
    def get(self, request, format=None):
        queryset = LoadImage.objects.all()
        serializer = LoadImageSerializers(
            queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "Error: url_img is required")
        files = request.data['url_img']
        name, form = os.path.splitext(files.name)
        request.data['name_img'] = name
        request.data['format_img'] = form
        serializer = LoadImageSerializers(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            img = LoadImage(**validated_data)
            img.save()
            serializer_response = LoadImageSerializers(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoadImageTableDetail(APIView):
    def get_object(self, pk):
        try:
            return LoadImage.objects.get(pk=pk)
        except LoadImage.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = LoadImageSerializers(idResponse)
            return Response(idResponse.data, status=status.HTTP_200_OK)
        return Response("error: no file found", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        files = request.data['url_img']
        name, form = os.path.splitext(files.name)
        request.data['name_img'] = name
        request.data['format_img'] = form
        serializer = LoadImageSerializers(idResponse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        imagen = self.get_object(pk)
        if imagen != 0:
            imagen.url_img.delete(save=True)
            imagen.delete()
            return Response("file deleted", status=status.HTTP_204_NO_CONTENT)
        return Response("error: file not found", status=status.HTTP_400_BAD_REQUEST)