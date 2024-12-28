from dataclasses import dataclass
from datetime import datetime

@dataclass
class Subscription:
    id: int
    member_id: int
    plan_type: str  # e.g., Monthly, Quarterly, Annual
    start_date: datetime
    end_date: datetime
    status: str  # e.g., Active, Inactive
    discount: float

    @staticmethod
    def from_dict(data):
        return Subscription(
            id=int(data['id']),
            member_id=int(data['member_id']),
            plan_type=data['plan_type'],
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d'),
            status=data['status'],
            discount=float(data['discount'])
        )

    def to_dict(self):
        return {
            'id': self.id,
            'member_id': self.member_id,
            'plan_type': self.plan_type,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'status': self.status,
            'discount': self.discount
        }