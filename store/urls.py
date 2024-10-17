from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('atualiza_usuario', views.atualiza_usuario, name='atualiza_usuario'),
    path('produtos/<int:pk>', views.produto, name='produto'),
]
