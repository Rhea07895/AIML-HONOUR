from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


class RazorpayCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return self.card_number

    def pay(self, amount):
        print("Razorpay Card Payment")
        print("Amount:", amount)
        return True


class RazorpayUPIPayment(PaymentMethod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return self.upi_id

    def pay(self, amount):
        print("Razorpay UPI Payment")
        print("Amount:", amount)
        return True


class StripeCardPayment(PaymentMethod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return self.card_number

    def pay(self, amount):
        print("Stripe Card Payment")
        print("Amount:", amount)
        return True


class StripeUPIPayment(PaymentMethod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return self.upi_id

    def pay(self, amount):
        print("Stripe UPI Payment")
        print("Amount:", amount)
        return True


class FactoryPaymentMethod:

    factory = {}

    @classmethod
    def get_payment_object(cls, method_type, **kwargs):
        if method_type not in cls.factory:
            raise ValueError("Invalid payment method")

        return cls.factory[method_type](**kwargs)


class RazorpayFactory(FactoryPaymentMethod):

    factory = {
        "card": RazorpayCardPayment,
        "upi": RazorpayUPIPayment
    }


class StripeFactory(FactoryPaymentMethod):

    factory = {
        "card": StripeCardPayment,
        "upi": StripeUPIPayment
    }


class Aggregator(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def call_get_payment_object(self, method_type, amount, **kwargs):
        pass


class RazorpayAggregator(Aggregator):

    processing_fee = 2.0

    def __init__(self):
        super().__init__("Razorpay")

    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = RazorpayFactory.get_payment_object(
            method_type, **kwargs
        )

        print("Gateway:", self.name)
        print("Fee:", self.processing_fee, "%")
        print("Details:", payment.get_details())

        return payment.pay(amount)


class StripeAggregator(Aggregator):

    processing_fee = 2.9

    def __init__(self):
        super().__init__("Stripe")

    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = StripeFactory.get_payment_object(
            method_type, **kwargs
        )

        print("Gateway:", self.name)
        print("Fee:", self.processing_fee, "%")
        print("Details:", payment.get_details())

        return payment.pay(amount)


class AggregatorFactory:

    factory = {
        "stripe": StripeAggregator,
        "razorpay": RazorpayAggregator
    }

    @classmethod
    def get_aggregator_object(cls, name):
        if name not in cls.factory:
            raise ValueError("Invalid aggregator")

        return cls.factory[name]()


def main():

    print("1. Stripe")
    print("2. Razorpay")

    aggregator_name = input("Enter aggregator: ").lower()

    aggregator = AggregatorFactory.get_aggregator_object(
        aggregator_name
    )

    method = input("Enter method (card/upi): ").lower()

    if method == "card":
        card = input("Enter card number: ")
        details = {"card_number": card}

    elif method == "upi":
        upi = input("Enter UPI ID: ")
        details = {"upi_id": upi}

    else:
        print("Invalid method")
        return

    amount = float(input("Enter amount: "))

    result = aggregator.call_get_payment_object(
        method,
        amount,
        **details
    )

    if result:
        print("Payment Successful")
    else:
        print("Payment Failed")


main()