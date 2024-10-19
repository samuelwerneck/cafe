from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('atualiza_senha', views.atualiza_senha, name='atualiza_senha'),
    path('atualiza_usuario', views.atualiza_usuario, name='atualiza_usuario'),
    path('atualiza_info', views.atualiza_info, name='atualiza_info'),
    path('produtos/<int:pk>', views.produto, name='produto'),
    path('busca/', views.busca, name='busca'),
]
