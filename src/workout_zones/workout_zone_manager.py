from src.database.csv_handler import read_csv, write_csv
from src.workout_zones.workout_zone import WorkoutZone

class WorkoutZoneManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fieldnames = ['id', 'name', 'exercise_types', 'attendant_name', 'updates', 'class_schedule', 'promotions']
        self.workout_zones = self.load_workout_zones()

    def load_workout_zones(self):
        data = read_csv(self.csv_file)
        return [WorkoutZone.from_dict(item) for item in data]

    def save_workout_zones(self):
        data = [zone.to_dict() for zone in self.workout_zones]
        write_csv(self.csv_file, self.fieldnames, data)

    def add_workout_zone(self, zone):
        self.workout_zones.append(zone)
        self.save_workout_zones()

    def remove_workout_zone(self, zone_id):
        self.workout_zones = [zone for zone in self.workout_zones if zone.id != zone_id]
        self.save_workout_zones()

    def update_workout_zone(self, updated_zone):
        for i, zone in enumerate(self.workout_zones):
            if zone.id == updated_zone.id:
                self.workout_zones[i] = updated_zone
                self.save_workout_zones()
                break