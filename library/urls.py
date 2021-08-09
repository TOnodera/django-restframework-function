from django.urls import path
from .views import LibraryAPIView, LibraryListAPIView

urlpatterns = [
    path('library/create', LibraryAPIView.as_view()),
    path('library/', LibraryListAPIView.as_view())
]
