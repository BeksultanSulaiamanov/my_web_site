from django.urls import path
from fruits import views
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('add_fruit/', views.add_fruit, name='add_fruit'),
]