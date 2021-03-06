from django.urls import path
from .views import LibraryCreateAPIView, LibraryDestroyAPIView, LibraryListAPIView, LibraryRetriveAPIView, BookCreateAPIView

urlpatterns = [
    path('libraries/create', LibraryCreateAPIView.as_view()),
    path('libraries/', LibraryListAPIView.as_view()),
    path('libraries/<pk>', LibraryRetriveAPIView.as_view()),
    path('libraries/<pk>', LibraryDestroyAPIView.as_view()),
    path('books/create', BookCreateAPIView.as_view()),
]
