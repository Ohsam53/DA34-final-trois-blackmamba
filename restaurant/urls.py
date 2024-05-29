from django.urls import path
from . import views

app_name = 'restaurant'  # URL 네임스페이스 지정
urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('create/', views.restaurant_create, name='restaurant_create'),
]
