from decimal import Decimal
from typing import Iterable

from django.db.models.signals import pre_save
from django.dispatch import receiver
from payments import PurchasedItem
from payments.models import BasePayment

from djangoProject1.settings import PAYMENT_HOST
from django.db import models

from socialnetwork.models import User


class Payment(BasePayment):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default='')
    price = models.DecimalField(max_digits=10000, decimal_places=2, default=0)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_expiry_date = models.DateField(blank=True, null=True)
    card_holder_name = models.CharField(max_length=255, blank=True, null=True)


@receiver(pre_save, sender=Payment)
def populate_payment_fields(sender, instance, **kwargs):
    user = instance.user
    if user:
        instance.card_number = user.card_number
        instance.card_expiry_date = user.card_expiry_date
        instance.card_holder_name = user.card_holder_name


def get_failure_url(self) -> str:
    print(self.price)
    print('get_failure_url')

    return f"http://{PAYMENT_HOST}/payments/{self.pk}/failure"


def get_success_url(self) -> str:
    print(self.price)
    print('get_success_url')

    return f"http://{PAYMENT_HOST}/payments/{self.pk}/success"


def get_purchased_items(self) -> Iterable[PurchasedItem]:
    print(self.price)
    print('get_purchased_items')
    yield PurchasedItem(
        name='Donate for Ukrainian military',
        sku='DFUM',
        price=Decimal(self.price),
        quantity=1,
        currency=self.currency,
    )
