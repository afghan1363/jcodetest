from django.urls import path
from . import views

app_name = 'wallet'


urlpatterns = [
    path('wallets/<uuid:uuid>/operation/', view=views.UpdateAPIView.as_view(),
         name='transaction'),
    path('wallets/<uuid:uuid>/', view=views.RetrieveAPIView.as_view(), name='wallet_detail'),
    path('wallets/all/', view=views.WalletListAPIView.as_view(), name='wallet_list')
]