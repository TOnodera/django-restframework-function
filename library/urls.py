from django.urls import path
from .views import LibraryCreateAPIView, LibraryListAPIView, LibraryRetriveAPIView

urlpatterns = [
    path('libraries/create', LibraryCreateAPIView.as_view()),
    path('libraries/', LibraryListAPIView.as_view()),
    path('libraries/<pk:int>', LibraryRetriveAPIView.as_view())
]
