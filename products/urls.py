from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('new/', views.new),
    path('', views.index, name='index' ),
    

]