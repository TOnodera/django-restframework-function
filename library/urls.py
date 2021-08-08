from .views import BookAPIView
from django.urls import path

urlpatterns = [
    path('books/', BookAPIView.as_view())
]
