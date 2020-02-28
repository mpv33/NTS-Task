from django.urls import path
from . import views

urlpatterns = [
    path('', views.tablet, name='tablet'),
    path('<int:medicine_id>/', views.detials, name='detials'),
]