from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('pine-lumber/', views.pine_lumber, name='pine_lumber'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('health/', views.health_check, name='health_check'),
]
