import pytest
from datetime import datetime
from src.staff_management.staff_manager import StaffManager
from src.staff_management.membership_growth import MembershipGrowth
from src.staff_management.revenue_trends import RevenueTrends
from src.staff_management.trainer_schedules import TrainerSchedule
from src.staff_management.equipment_maintenance import EquipmentMaintenance

@pytest.fixture
def staff_manager():
    return StaffManager(membership_csv="../data/membership_growth.csv", revenue_csv="../data/revenue_trends.csv", schedules_csv="../data/trainers_schedule.csv", maintenance_csv="../data/equipment_maintenance.csv")


def test_add_membership_record(staff_manager):
    record = MembershipGrowth(id=1, date=datetime.strptime("2024-12-20", "%Y-%m-%d"), new_members=5, total_members=105)
    staff_manager.membership_records.append(record)
    staff_manager.save_membership_records()

def test_remove_membership_record(staff_manager):
    record = MembershipGrowth(id=1, date=datetime.strptime("2024-12-20", "%Y-%m-%d"), new_members=5, total_members=105)
    staff_manager.membership_records.append(record)
    staff_manager.save_membership_records()
    staff_manager.membership_records = [r for r in staff_manager.membership_records if r.id != 1]
    staff_manager.save_membership_records()

def test_update_membership_record(staff_manager):
    record = MembershipGrowth(id=1, date=datetime.strptime("2024-12-20", "%Y-%m-%d"), new_members=5, total_members=105)
    staff_manager.membership_records.append(record)
    staff_manager.save_membership_records()
    updated_record = MembershipGrowth(id=1, date=datetime.strptime("2024-12-20", "%Y-%m-%d"), new_members=7, total_members=112)
    for i, r in enumerate(staff_manager.membership_records):
        if r.id == updated_record.id:
            staff_manager.membership_records[i] = updated_record
            break
    staff_manager.save_membership_records()

def test_add_revenue_record(staff_manager):
    record = RevenueTrends(id=1, date=datetime.strptime("2024-12-20", "%Y-%m-%d"), revenue=500.0)
    staff_manager.revenue_records.append(record)
    staff_manager.save_revenue_records()

def test_remove_revenue_record(staff_manager):
    record = RevenueTrends(id=1, date=datetime.strptime("2024-12-20", "%Y-%m-%d"), revenue=500.0)
    staff_manager.revenue_records.append(record)
    staff_manager.save_revenue_records()
    staff_manager.revenue_records = [r for r in staff_manager.revenue_records if r.id != 1]
    staff_manager.save_revenue_records()

def test_update_revenue_record(staff_manager):
    record = RevenueTrends(id=1, date=datetime.strptime("2024-12-20", "%Y-%m-%d"), revenue=500.0)
    staff_manager.revenue_records.append(record)
    staff_manager.save_revenue_records()
    updated_record = RevenueTrends(id=1, date=datetime.strptime("2024-12-20", "%Y-%m-%d"), revenue=600.0)
    for i, r in enumerate(staff_manager.revenue_records):
        if r.id == updated_record.id:
            staff_manager.revenue_records[i] = updated_record
            break
    staff_manager.save_revenue_records()

def test_add_schedule_record(staff_manager):
    schedule = TrainerSchedule(id=1, trainer_id=101, trainer_name="John Doe", class_name="Yoga", start_time=datetime.strptime("08:00:00","%H:%M:%S"), end_time=datetime.strptime("08:00:00","%H:%M:%S"))
    staff_manager.schedules_records.append(schedule)
    staff_manager.save_schedules_records()

def test_remove_schedule_record(staff_manager):
    schedule = TrainerSchedule(id=1, trainer_id=101, trainer_name="John Doe", class_name="Yoga", start_time=datetime.strptime("08:00:00","%H:%M:%S"), end_time=datetime.strptime("08:00:00","%H:%M:%S"))
    staff_manager.schedules_records.append(schedule)
    staff_manager.save_schedules_records()
    staff_manager.schedules_records = [s for s in staff_manager.schedules_records if s.id != 1]
    staff_manager.save_schedules_records()

def test_update_schedule_record(staff_manager):
    schedule = TrainerSchedule(id=1, trainer_id=101, trainer_name="John Doe", class_name="Yoga", start_time=datetime.strptime("08:00:00","%H:%M:%S"), end_time=datetime.strptime("08:00:00","%H:%M:%S"))
    staff_manager.schedules_records.append(schedule)
    staff_manager.save_schedules_records()
    updated_schedule = TrainerSchedule(id=1, trainer_id=101, trainer_name="John Doe", class_name="Pilates", start_time=datetime.strptime("08:00:00","%H:%M:%S"), end_time=datetime.strptime("08:00:00","%H:%M:%S"))
    for i, s in enumerate(staff_manager.schedules_records):
        if s.id == updated_schedule.id:
            staff_manager.schedules_records[i] = updated_schedule
            break
    staff_manager.save_schedules_records()

def test_add_maintenance_record(staff_manager):
    maintenance = EquipmentMaintenance(id=1, equipment_name="Treadmill", last_maintenance=datetime.strptime("2024-12-20", "%Y-%m-%d"), next_maintenance=datetime.strptime("2024-12-20", "%Y-%m-%d"), status="Completed")
    staff_manager.maintenance_records.append(maintenance)
    staff_manager.save_maintenance_records()

def test_remove_maintenance_record(staff_manager):
    maintenance = EquipmentMaintenance(id=1, equipment_name="Treadmill", last_maintenance=datetime.strptime("2024-12-20", "%Y-%m-%d"), next_maintenance=datetime.strptime("2024-12-20", "%Y-%m-%d"), status="Completed")
    staff_manager.maintenance_records.append(maintenance)
    staff_manager.save_maintenance_records()
    staff_manager.maintenance_records = [m for m in staff_manager.maintenance_records if m.id != 1]
    staff_manager.save_maintenance_records()

def test_update_maintenance_record(staff_manager):
    maintenance = EquipmentMaintenance(id=1, equipment_name="Treadmill", last_maintenance=datetime.strptime("2024-12-20", "%Y-%m-%d"), next_maintenance=datetime.strptime("2024-12-20", "%Y-%m-%d"), status="Completed")
    staff_manager.maintenance_records.append(maintenance)
    staff_manager.save_maintenance_records()
    updated_maintenance = EquipmentMaintenance(id=1, equipment_name="Treadmill", last_maintenance=datetime.strptime("2024-12-20", "%Y-%m-%d"), next_maintenance=datetime.strptime("2024-12-20", "%Y-%m-%d"), status="Pending")
    for i, m in enumerate(staff_manager.maintenance_records):
        if m.id == updated_maintenance.id:
            staff_manager.maintenance_records[i] = updated_maintenance
            break
    staff_manager.save_maintenance_records()