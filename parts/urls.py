from django.urls import path
from . import views

urlpatterns = [
    path('', views.parts, name="parts"),
    path('part_detail/', views.part_detail, name="part_detail"),
]
