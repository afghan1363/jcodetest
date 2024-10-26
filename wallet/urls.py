from django.urls import path
from . import views


urlpatterns = [
    path('wallets/<WALLET_UUID:wallet_uuid>/operation/', view=views.UpdateAPIView.as_view(),
         name='transaction'),
    path('wallets/<WALLET_UUID:wallet_uuid>/', view=views.RetrieveAPIView.as_view()),
    path('wallets/all/')
]