from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404, UpdateAPIView

from . import serializers
from .models import Wallet
from .permissions import IsOwner

class WalletListAPIView(ListAPIView):
    serializer_class = serializers.GetBalanceSerializer

    def get_queryset(self):
        return Wallet.objects.filter(owner=self.request.user.pk)
    

class WalletRetrieveAPIView(RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = serializers.GetBalanceSerializer
    permission_classes = (IsOwner,)

    def get_object(self, *args, **kwargs):
        uuid = self.kwargs.get('WALLET_UUID')
        obj = get_object_or_404(self.queryset, wallet_uuid=uuid)
        return obj
    

class WalletUpdateAPIView(UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = serializers.WalletTransSerializer
    permission_classes = (IsOwner,)

    def get_object(self, *args, **kwargs):
        uuid = self.kwargs.get('WALLET_UUID')
        obj = get_object_or_404(self.queryset, wallet_uuid=uuid)
        return obj
