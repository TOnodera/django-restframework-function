from django.conf import settings
from rest_framework import serializers, status, views
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import LibrarySerializer

class LibraryAPIView(views.APIView):

    def post(self, request: Request, *args, **kwargs):
        serializer = LibrarySerializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
