from src.database.csv_handler import read_csv, write_csv
from src.payments.payment import Payment
from src.payments.subscription import Subscription


class PaymentManager:
    def __init__(self, payments_csv_file, subscriptions_csv_file):
        self.payments_csv_file = payments_csv_file
        self.subscriptions_csv_file = subscriptions_csv_file

        self.payment_fieldnames = ['id', 'member_id', 'amount', 'date', 'payment_method', 'description']
        self.subscription_fieldnames = ['id', 'member_id', 'plan_type', 'start_date', 'end_date', 'status', 'discount']

        self.payments = self.load_payments()
        self.subscriptions = self.load_subscriptions()

    def load_payments(self):
        data = read_csv(self.payments_csv_file)
        return [Payment.from_dict(item) for item in data]

    def save_payments(self):
        data = [payment.to_dict() for payment in self.payments]
        write_csv(self.payments_csv_file, self.payment_fieldnames, data)

    def load_subscriptions(self):
        data = read_csv(self.subscriptions_csv_file)
        return [Subscription.from_dict(item) for item in data]

    def save_subscriptions(self):
        data = [subscription.to_dict() for subscription in self.subscriptions]
        write_csv(self.subscriptions_csv_file, self.subscription_fieldnames, data)

    def add_payment(self, payment):
        self.payments.append(payment)
        self.save_payments()

    def remove_payment(self, payment_id):
        self.payments = [payment for payment in self.payments if payment.id != payment_id]
        self.save_payments()

    def update_payment(self, updated_payment):
        for i, payment in enumerate(self.payments):
            if payment.id == updated_payment.id:
                self.payments[i] = updated_payment
                self.save_payments()
                break

    def add_subscription(self, subscription):
        self.subscriptions.append(subscription)
        self.save_subscriptions()

    def remove_subscription(self, subscription_id):
        self.subscriptions = [subscription for subscription in self.subscriptions if subscription.id != subscription_id]
        self.save_subscriptions()

    def update_subscription(self, updated_subscription):
        for i, subscription in enumerate(self.subscriptions):
            if subscription.id == updated_subscription.id:
                self.subscriptions[i] = updated_subscription
                self.save_subscriptions()
                break