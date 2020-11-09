from django.urls import path
from site_one import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:tvno>',views.index, name='tv-url'),

]