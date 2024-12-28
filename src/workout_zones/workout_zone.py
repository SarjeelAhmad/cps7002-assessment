from dataclasses import dataclass

@dataclass
class WorkoutZone:
    id: int
    name: str
    exercise_types: str  # Comma-separated list of exercise types
    attendant_name: str
    updates: str  # Important updates
    class_schedule: str  # Class schedules
    promotions: str  # Promotions

    @staticmethod
    def from_dict(data):
        return WorkoutZone(
            id=int(data['id']),
            name=data['name'],
            exercise_types=data['exercise_types'],
            attendant_name=data['attendant_name'],
            updates=data['updates'],
            class_schedule=data['class_schedule'],
            promotions=data['promotions']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'exercise_types': self.exercise_types,
            'attendant_name': self.attendant_name,
            'updates': self.updates,
            'class_schedule': self.class_schedule,
            'promotions': self.promotions
        }