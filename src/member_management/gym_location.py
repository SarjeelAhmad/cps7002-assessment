from dataclasses import dataclass

@dataclass
class GymLocation:
    id: int
    city: str
    address: str
    manager_name: str
    workout_zones: str  # Comma-separated list of workout zones

    @staticmethod
    def from_dict(data):
        return GymLocation(
            id=int(data['id']),
            city=data['city'],
            address=data['address'],
            manager_name=data['manager_name'],
            workout_zones=data['workout_zones']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
            'address': self.address,
            'manager_name': self.manager_name,
            'workout_zones': self.workout_zones
        }