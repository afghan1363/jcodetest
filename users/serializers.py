from rest_framework.serializers import ModelSerializer, IntegerField, CharField
from .models import User
from wallet.models import Wallet
from wallet.serializers import NewWalletSerializer


class UserSerializer(ModelSerializer):
    """
    Сериализатор модели User
    """
    password = CharField(min_length=8, write_only=True)
    wallet = NewWalletSerializer

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        wallet = Wallet.objects.create(
            owner=user
        )
        wallet.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'full_name', 'phone')
