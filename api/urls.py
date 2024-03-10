from django.urls import path
from .views import BookAPIView,CustomAuthToken

urlpatterns = [
    path('',BookAPIView.as_view()),

]