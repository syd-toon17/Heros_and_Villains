from django.urls import path
from . import views

urlpatterns = [
    path('', views.battle_date_list),
    path('<int:pk>/', views.battle_date_detail),
]