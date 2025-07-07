from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('durability-testing/', views.durability_testing, name='durability_testing'),
    path('category/<slug:slug>/', views.CategoryProductListView.as_view(), name='category'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='detail'),
]
