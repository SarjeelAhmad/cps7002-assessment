from dataclasses import dataclass
from datetime import datetime

@dataclass
class Appointment:
    id: int
    member_id: int
    trainer_id: int
    appointment_type: str  # Personal Training, Group Class, Consultation
    date_time: datetime
    status: str  # Scheduled, Cancelled

    @staticmethod
    def from_dict(data):
        return Appointment(
            id=int(data['id']),
            member_id=int(data['member_id']),
            trainer_id=int(data['trainer_id']),
            appointment_type=data['appointment_type'],
            date_time=datetime.strptime(data['date_time'], '%Y-%m-%d %H:%M:%S'),
            status=data['status']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'member_id': self.member_id,
            'trainer_id': self.trainer_id,
            'appointment_type': self.appointment_type,
            'date_time': self.date_time.strftime('%Y-%m-%d %H:%M:%S'),
            'status': self.status
        }