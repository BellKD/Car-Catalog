from django .urls import path
from .import views

urlpatterns = [
    path('', views.index_view,name='index'),
    path('car/<int:pk>/', views.car_detail_view, name='car_detail'),
]

