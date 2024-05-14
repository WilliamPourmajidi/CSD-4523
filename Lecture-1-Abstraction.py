class PaymentProcessor:
    def __init__(self, payment_data):
        self.payment_data = payment_data

    def process_payment(self):
        if self.payment_data['type'] == 'credit':
            return self._process_credit_card()
        elif self.payment_data['type'] == 'paypal':
            return self._process_paypal()

    def _process_credit_card(self):
        # Simulate credit card processing
        print(f"Processing credit card payment for {self.payment_data['amount']}")
        return "Credit card processed"

    def _process_paypal(self):
        # Simulate PayPal processing
        print(f"Processing PayPal payment for {self.payment_data['amount']}")
        return "PayPal processed"

# Usage
payment_processor = PaymentProcessor({'type': 'credit', 'amount': 100})
print(payment_processor.process_payment())
