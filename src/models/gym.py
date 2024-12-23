# src/models/gym.py

class GymLocation:
    def __init__(self, gym_id, name, city, address, manager_name):
        """
        Initializes a new GymLocation instance.
        :param gym_id: Unique identifier for the gym location
        :param name: Name of the gym location
        :param city: City where the gym is located
        :param address: Full address of the gym
        :param manager_name: Name of the gym manager
        """
        self.gym_id = gym_id
        self.name = name
        self.city = city
        self.address = address
        self.manager_name = manager_name
        self.workout_zones = []

    def add_workout_zone(self, workout_zone):
        """
        Adds a workout zone to the gym location.
        :param workout_zone: WorkoutZone instance
        """
        self.workout_zones.append(workout_zone)

    def remove_workout_zone(self, zone_id):
        """
        Removes a workout zone by its ID.
        :param zone_id: Unique identifier for the workout zone
        """
        self.workout_zones = [zone for zone in self.workout_zones if zone.zone_id != zone_id]

    def get_info(self):
        """
        Retrieves gym location details as a dictionary.
        :return: Dictionary with gym details
        """
        return {
            "gym_id": self.gym_id,
            "name": self.name,
            "city": self.city,
            "address": self.address,
            "manager_name": self.manager_name,
            "workout_zones": [zone.get_info() for zone in self.workout_zones],
        }
