# Define a class to represent the payment processor
class PaymentProcessor:
    def __init__(self):
        self.transfers = []

    # Method to add a new transfer
    def add_transfer(self, amount, recipient):
        transfer = {
            "amount": amount,
            "recipient": recipient
        }
        self.transfers.append(transfer)

    # Method to get all transfers
    def get_transfers(self):
        return self.transfers

    # Method to get the total amount transferred
    def get_total_amount(self):
        return sum([transfer["amount"] for transfer in self.transfers])

# Create a payment processor instance
payment_processor = PaymentProcessor()

# Add some transfers
payment_processor.add_transfer(100, "John")
payment_processor.add_transfer(200, "Jane")
payment_processor.add_transfer(50, "Bob")

# Get all transfers
transfers = payment_processor.get_transfers()
print("Transfers:")
for transfer in transfers:
    print(f"Amount: {transfer['amount']}, Recipient: {transfer['recipient']}")

# Get the total amount transferred
total_amount = payment_processor.get_total_amount()
print(f"\nTotal Amount: {total_amount}")