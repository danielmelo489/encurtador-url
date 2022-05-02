from django.urls import path
from . import views

app_name='core'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:slug>', views.go, name='go')
]