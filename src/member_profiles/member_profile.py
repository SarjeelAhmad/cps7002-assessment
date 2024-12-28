from dataclasses import dataclass

@dataclass
class MemberProfile:
    id: int
    name: str
    age: int
    gender: str
    membership_type: str  # Regular, Premium, Trial
    health_info: str
    membership_status: str  # Active, Inactive

    @staticmethod
    def from_dict(data):
        return MemberProfile(
            id=int(data['id']),
            name=data['name'],
            age=int(data['age']),
            gender=data['gender'],
            membership_type=data['membership_type'],
            health_info=data['health_info'],
            membership_status=data['membership_status']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'membership_type': self.membership_type,
            'health_info': self.health_info,
            'membership_status': self.membership_status
        }