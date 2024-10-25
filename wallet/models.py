from django.db import models
import uuid

from django.conf import settings
from django.utils.translation import gettext_lazy as _



class Wallet(models.Model):
    wallet_uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name="UUID")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              verbose_name=_("Account holder"))
    balance = models.DecimalField(max_digits=11, decimal_places=2, default=0.00, verbose_name=_("Balance"))

    def __str__(self):
        return f'Owner: {self.owner}, Wallet: {self.wallet_uuid}'