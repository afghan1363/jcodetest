from rest_framework.serializers import ModelSerializer, CharField, IntegerField, ValidationError
from .models import Wallet


class WalletTransSerializer(ModelSerializer):
    operation = CharField(max_length=8)
    amount = IntegerField(min_value=10)

    class Meta:
        model = Wallet
        fields = ('operation', 'amount')

    def validate_operation(self, value):
        if value not in ('WITHDRAW', 'DEPOSIT'):
            raise ValidationError('Wrong operation')
        return value

    def update(self, instance, validated_data):        
        if validated_data.get('operation') == 'WITHDRAW' and instance.balance >= self.amount:
            instance.balance -= self.amount
        elif validated_data.get('operation') == 'WITHDRAW' and instance.balance < self.amount:
            raise ValidationError("You have not enough money")
        elif validated_data.get('operation') == 'DEPOSIT':
            instance.balance += self.amount
        instance.save()
        return instance
    

class GetBalanceSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'


class NewWalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('owner',)
