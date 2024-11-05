from django.urls import path

from workspace import views

urlpatterns = [
    path('create/', views.creatSneakers, name='creat'),
    path('update/<int:id>/', views.updateSneakers, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('', views.main, name='workspace'),
]
