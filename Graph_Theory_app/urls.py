from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index,name = 'index'),
    path("first/", views.first,name = 'first'),
    path("prim/", views.prim,name = 'prim'),
    path("warshall/", views.warshall,name = 'warshall'),
    path("warshall/", views.warshall,name = 'warshall'),
    path('save_matrix_data', views.save_matrix_data, name='save_matrix_data'),
]