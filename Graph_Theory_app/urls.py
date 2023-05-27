from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index,name = 'index'),
    path('save_matrix_data', views.save_matrix_data, name='save_matrix_data'),
]