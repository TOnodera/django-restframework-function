from threading import main_thread
from rest_framework import fields, serializers, status, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import LibrarySerializer
from django_filters import rest_framework as filters
from .models import Library

class LibraryAPIView(views.APIView):

    def post(self, request: Request, *args, **kwargs):
        serializer = LibrarySerializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class LibraryFilter(filters.FilterSet):
    class Meta:
        model = Library
        fields = '__all__'

class LibraryListAPIView(views.APIView):

    def get(self, request: Request, *args, **kwargs):

        filterset = LibraryFilter(request.query_params, queryset=Library.objects.all())
        if not filterset.is_valid():
            raise ValidationError(filterset.errors)
        serializer = LibrarySerializer(instance=filterset.qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
