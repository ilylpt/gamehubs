from django.urls import path
from . import views

app_name = 'kategoriler'

urlpatterns = [
    path('', views.categories_list, name='kategoriler'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:game_slug>/', views.game_detail, name='game_detail'),
]
