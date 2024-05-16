from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View
from socialnetwork.serializers.payment.payment import PaymentSerializer
from socialnetwork.utilities.payment.payment import create_dummy_payment


class PaymentView(View):
    def post(self, request):
        serializer = PaymentSerializer(data=request.POST)
        if serializer.is_valid():
            price = serializer.data['price']
            variant = serializer.data['variant']
            currency = serializer.data['currency']
            payment = create_dummy_payment(price, variant, currency, request.user)
            print(payment)
            return TemplateResponse(
                request,
                'templates/payment/payment.html',
                {'payment': payment}
            )
        return HttpResponse(serializer.errors, status=400)
