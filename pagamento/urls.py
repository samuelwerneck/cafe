from django.urls import path
from . import views

urlpatterns = [
    path('pagamento_sucesso', views.pagamento_sucesso, name='pagamento_sucesso'),
    path('checkout', views.checkout, name='checkout'),
    path('pagamento_info', views.pagamento_info, name='pagamento_info'),
    path('processa_pedido', views.processa_pedido, name='processa_pedido'),
    path('painel_enviados', views.painel_enviados, name='painel_enviados'),
    path('painel_nao_enviados', views.painel_nao_enviados, name='painel_nao_enviados'),
    path('pedidos/<int:pk>', views.pedidos, name='pedidos'),
]