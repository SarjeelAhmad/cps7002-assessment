from dataclasses import dataclass
from datetime import datetime

@dataclass
class Payment:
    id: int
    member_id: int
    amount: float
    date: datetime
    payment_method: str  # e.g., Credit Card, PayPal, Cash
    description: str
    status: str  # e.g., Completed, Pending

    @staticmethod
    def from_dict(data):
        return Payment(
            id=int(data['id']),
            member_id=int(data['member_id']),
            amount=float(data['amount']),
            date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'),
            payment_method=data['payment_method'],
            description=data['description'],
            status=data['status']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'member_id': self.member_id,
            'amount': self.amount,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S'),
            'payment_method': self.payment_method,
            'description': self.description,
            'status': self.status
        }