from django.urls import path
from .views import LibraryAPIView

urlpatterns = [
    path('library/', LibraryAPIView.as_view())
]
