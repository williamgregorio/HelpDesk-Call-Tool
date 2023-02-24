from django.urls import path
from .views import LogView

urlpatterns = [
    path('home', LogView.as_view()),
]