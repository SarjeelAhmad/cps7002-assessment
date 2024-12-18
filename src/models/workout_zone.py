# src/models/workout_zone.py

class WorkoutZone:
    def __init__(self, zone_id, name, category, equipment_list, attendant_name):
        """
        Initializes a new WorkoutZone instance.
        :param zone_id: Unique identifier for the workout zone
        :param name: Name of the workout zone
        :param category: Type/category of the workout zone (e.g., cardio, weightlifting)
        :param equipment_list: List of equipment available in the workout zone
        :param attendant_name: Name of the zone attendant
        """
        self.zone_id = zone_id
        self.name = name
        self.category = category
        self.equipment_list = equipment_list
        self.attendant_name = attendant_name
        self.schedules = []

    def add_schedule(self, schedule):
        """
        Adds a schedule to the workout zone.
        :param schedule: Dictionary containing schedule details
        """
        self.schedules.append(schedule)

    def remove_schedule(self, schedule_id):
        """
        Removes a schedule by its ID.
        :param schedule_id: Unique identifier for the schedule
        """
        self.schedules = [schedule for schedule in self.schedules if schedule["id"] != schedule_id]

    def get_info(self):
        """
        Retrieves workout zone details as a dictionary.
        :return: Dictionary with workout zone details
        """
        return {
            "zone_id": self.zone_id,
            "name": self.name,
            "category": self.category,
            "equipment_list": self.equipment_list,
            "attendant_name": self.attendant_name,
            "schedules": self.schedules,
        }
