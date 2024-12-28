import pytest
from src.workout_zones.workout_zone_manager import WorkoutZoneManager
from src.workout_zones.workout_zone import WorkoutZone

@pytest.fixture
def workout_zone_manager():
    return WorkoutZoneManager(csv_file="../data/workout_zones.csv")

def test_add_workout_zone(workout_zone_manager):
    zone = WorkoutZone(id=3, name="Flexibility Zone", exercise_types="Stretching", attendant_name="Emily Clark", updates="Update 3", class_schedule="Schedule 3", promotions="Promotion 3")
    workout_zone_manager.add_workout_zone(zone)

def test_remove_workout_zone(workout_zone_manager):
    zone = WorkoutZone(id=3, name="Flexibility Zone", exercise_types="Stretching", attendant_name="Emily Clark", updates="Update 3", class_schedule="Schedule 3", promotions="Promotion 3")
    workout_zone_manager.add_workout_zone(zone)
    workout_zone_manager.remove_workout_zone(3)

def test_update_workout_zone(workout_zone_manager):
    zone = WorkoutZone(id=3, name="Flexibility Zone", exercise_types="Stretching", attendant_name="Emily Clark", updates="Update 3", class_schedule="Schedule 3", promotions="Promotion 3")
    workout_zone_manager.add_workout_zone(zone)
    updated_zone = WorkoutZone(id=3, name="Flexibility Zone", exercise_types="Yoga", attendant_name="Emily Clark", updates="Update 3", class_schedule="Schedule 3", promotions="Promotion 3")
    workout_zone_manager.update_workout_zone(updated_zone)