from django.urls import path
from . import views

urlpatterns = [
    path('', views.images, name = "imaginerium"),
    path('image/<str:pk>/', views.image, name = "image"),
    path('create-image/',views.createImage, name= "create-image"),
    path('update-image/<str:pk>/',views.updateImage, name='update-image'),
    path('delete-image/<str:pk>/',views.deleteImage, name='delete-image')
]
