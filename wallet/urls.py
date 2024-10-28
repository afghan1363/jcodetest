from django.urls import path
from . import views

app_name = 'wallet'


urlpatterns = [
    path('wallets/<uuid:uuid>/operation/', view=views.WalletUpdateAPIView.as_view(),
         name='transaction'),
    path('wallets/<uuid:uuid>/', view=views.WalletRetrieveAPIView.as_view(), name='wallet_detail'),
    path('wallets/all/', view=views.WalletListAPIView.as_view(), name='wallet_list')
]