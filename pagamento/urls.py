from django.urls import path
from . import views

urlpatterns = [
    path('pagamento_sucesso', views.pagamento_sucesso, name='pagamento_sucesso'),
    path('checkout', views.checkout, name='checkout'),
]