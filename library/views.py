from rest_framework import views, status
from rest_framework.response import Response
from .serializers import BookSerialiser

class BookAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerialiser
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
