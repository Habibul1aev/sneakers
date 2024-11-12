from django.urls import path

from workspace import views

urlpatterns = [
    path('create/', views.creatSneakers, name='creat'),
    path('update/<int:id>/', views.updateSneakers, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('login/', views.login_profile, name='login_profile'),
    path('registration/', views.regist_profile, name='regist_profile'),
    path('logout/', views.logout_profile, name='logout_profile'),
    path('', views.main, name='workspace'),
]
