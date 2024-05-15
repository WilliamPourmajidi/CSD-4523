class PaymentProcessor:
    # Initializes the PaymentProcessor class with payment_data dictionary.
    def __init__(self, payment_data):
        self.payment_data = payment_data

    # Main method to process payments based on payment type.
    def process_payment(self):
        # Validate payment data before proceeding.
        if not self._validate_payment():
            return "Invalid payment data"
        # Determine payment type and call the appropriate method.
        if self.payment_data['type'] == 'credit':
            return self._process_credit_card()
        elif self.payment_data['type'] == 'paypal':
            return self._process_paypal()

    # Private method to validate if all required fields are present.

    def _validate_payment(self):
        # List of required fields for the payment process.
        required_fields = ['type', 'amount']
        for field in required_fields:
            if field not in self.payment_data:
                print(f"Missing {field} in payment data")
                return False
        return True

    # Private method to simulate credit card payment processing.
    def _process_credit_card(self):
        # Output to simulate action and show amount being processed.
        print(f"Processing credit card payment for {self.payment_data['amount']}")
        return "Credit card processed"

    # Private method to simulate PayPal payment processing.
    def _process_paypal(self):
        # Output to simulate action and show amount being processed.
        print(f"Processing PayPal payment for {self.payment_data['amount']}")
        return "PayPal processed"

# Usage

# Create an instance of PaymentProcessor with specified payment data.
payment_processor = PaymentProcessor({'type': 'credit', 'amount': 100})
# Call the process_payment method and print the result.
print(payment_processor.process_payment())
