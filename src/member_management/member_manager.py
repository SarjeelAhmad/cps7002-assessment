from src.database.csv_handler import read_csv, write_csv
from src.member_management.gym_location import GymLocation

class MemberManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fieldnames = ['id', 'city', 'address', 'manager_name', 'workout_zones']
        self.locations = self.load_locations()

    def load_locations(self):
        data = read_csv(self.csv_file)
        return [GymLocation.from_dict(item) for item in data]

    def save_locations(self):
        data = [location.to_dict() for location in self.locations]
        write_csv(self.csv_file, self.fieldnames, data)

    def add_location(self, location):
        self.locations.append(location)
        self.save_locations()

    def remove_location(self, location_id):
        self.locations = [loc for loc in self.locations if loc.id != location_id]
        self.save_locations()

    def update_location(self, updated_location):
        for i, loc in enumerate(self.locations):
            if loc.id == updated_location.id:
                self.locations[i] = updated_location
                self.save_locations()
                break