from django.urls import path
from . import views

urlpatterns = [
    path('', views.RetrieveUpdateUserView.as_view()),
    path('register/', views.CreateUserview.as_view()),
    path('token/', views.CreateTokenView.as_view())
]
