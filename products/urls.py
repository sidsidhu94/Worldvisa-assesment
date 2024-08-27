from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateProductView.as_view(), name='product-create'),
]