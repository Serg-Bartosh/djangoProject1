from decimal import Decimal
from payments import get_payment_model


def create_dummy_payment(price, variant, currency, user):
    Payment = get_payment_model()

    payment = Payment.objects.create(
        user=user,
        variant=variant,
        description='Test Payment',
        total=1,
        price=Decimal(price),
        currency=currency,
        status='waiting'
    )

    return payment
