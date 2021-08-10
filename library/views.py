from functools import partial
from threading import main_thread
from rest_framework import fields, serializers, status, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import LibrarySerializer
from django_filters import rest_framework as filters
from django.shortcuts import get_object_or_404
from .models import Library
from drf_yasg.utils import swagger_auto_schema

class LibraryFilter(filters.FilterSet):
    class Meta:
        model = Library
        fields = '__all__'

class LibraryCreateAPIView(views.APIView):

    @swagger_auto_schema(
        request_body=LibrarySerializer
    )
    def post(self, request: Request, *args, **kwargs):
        serializer = LibrarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class LibraryListAPIView(views.APIView):

    @swagger_auto_schema(

    )
    def get(self, request: Request, *args, **kwargs):

        filterset = LibraryFilter(request.query_params, queryset=Library.objects.all())
        if not filterset.is_valid():
            raise ValidationError(filterset.errors)
        serializer = LibrarySerializer(instance=filterset.qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class LibraryRetriveAPIView(views.APIView):
    @swagger_auto_schema(

    )
    def get(self, request: Request, pk: int, *args, **kwargs):
        library = get_object_or_404(Library, pk=pk)
        serializer = LibrarySerializer(instance=library)
        return Response(serializer.data, status.HTTP_200_OK)

class LibraryUpdateAPIView(views.APIView):
    # 更新
    @swagger_auto_schema(
        request_body=LibrarySerializer
    )
    def put(self, request: Request, pk: int, *args, **kwargs):
        library = get_object_or_404(Library, pk=pk)
        serializer = LibrarySerializer(instance=library, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    # 部分更新（渡された値だけ更新する）
    @swagger_auto_schema(
        request_body=LibrarySerializer
    )
    def patch(self, request: Request, pk: int, *args, **kwargs):
        library = get_object_or_404(Library, pk=pk)
        serializer = LibrarySerializer(instance=library, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

class LibraryDestroyAPIView(views.APIView):
    @swagger_auto_schema(
        request_body=LibrarySerializer
    )
    def delete(self, request: Request, pk: int, *args, **kwargs):
        library = get_object_or_404(Library, pk=pk)
        library.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
