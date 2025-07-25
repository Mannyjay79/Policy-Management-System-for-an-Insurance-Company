class Payment:
    def __init__(self):
        self.payments = {}

    def process_payment(self, holder_id, amount):
        self.payments[holder_id] = self.payments.get(holder_id, 0) + amount
        print(f"Payment of {amount} processed for ID: {holder_id}")

    def reminder(self, holder_id):
        if holder_id not in self.payments:
            print(f"Reminder: No payment found for ID: {holder_id}")

    def apply_penalty(self, holder_id, penalty_amount):
        if holder_id in self.payments:
            self.payments[holder_id] -= penalty_amount
            print(f"Penalty of {penalty_amount} applied to ID: {holder_id}")