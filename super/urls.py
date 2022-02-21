from django.urls import path
from . import views

urlpatterns = [
    path('', views.super_list),
    # path('<init:pk>/', views.super_detail)
]