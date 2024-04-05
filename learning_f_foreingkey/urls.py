from django.urls import path
from . import views

app_name = 'learning_f_foreingkey'
urlpatterns = [
    path('send_to_santa/', views.send_to_santa_views, name='send_to_santa'),

]