from django.urls import path
from . import views

app_name = 'learning_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('input_one/', views.input_one, name='input_one'),
    path('list/', views.list_view, name='list'),
    path('delete_old_vacancy/', views.delete_old, name='delete'),
]
