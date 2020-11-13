from django.urls import path
from sign import views

urlpatterns = [
    path('',views.index, name='index'),
]