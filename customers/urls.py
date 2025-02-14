from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.customer_create, name='customer_create'),
    path('update/<int:pk>/', views.customer_update, name='customer_update'),
    path('list/', views.customer_list, name='customer_list'),
    path('detail/<int:pk>/', views.customer_detail, name='customer_detail'),
]
