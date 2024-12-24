from dataclasses import dataclass
from datetime import datetime

@dataclass
class Attendance:
    id: int
    member_id: int
    class_name: str
    check_in: datetime
    check_out: datetime

    @staticmethod
    def from_dict(data):
        return Attendance(
            id=int(data['id']),
            member_id=int(data['member_id']),
            class_name=data['class_name'],
            check_in=datetime.strptime(data['check_in'], '%Y-%m-%d %H:%M:%S'),
            check_out=datetime.strptime(data['check_out'], '%Y-%m-%d %H:%M:%S')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'member_id': self.member_id,
            'class_name': self.class_name,
            'check_in': self.check_in.strftime('%Y-%m-%d %H:%M:%S'),
            'check_out': self.check_out.strftime('%Y-%m-%d %H:%M:%S')
        }