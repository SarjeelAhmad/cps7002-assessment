from src.database.csv_handler import read_csv, write_csv
from src.staff_management.membership_growth import MembershipGrowth
from src.staff_management.revenue_trends import RevenueTrends
from src.staff_management.trainer_schedules import TrainerSchedule
from src.staff_management.equipment_maintenance import EquipmentMaintenance

class StaffManager:
    def __init__(self, membership_csv, revenue_csv, schedules_csv, maintenance_csv):
        self.membership_csv = membership_csv
        self.revenue_csv = revenue_csv
        self.schedules_csv = schedules_csv
        self.maintenance_csv = maintenance_csv

        self.membership_fieldnames = ['id', 'date', 'new_members', 'total_members']
        self.revenue_fieldnames = ['id', 'date', 'revenue']
        self.schedules_fieldnames = ['id', 'trainer_id', 'trainer_name', 'class_name', 'start_time', 'end_time']
        self.maintenance_fieldnames = ['id', 'equipment_name', 'last_maintenance', 'next_maintenance', 'status']

        self.membership_records = self.load_membership_records()
        self.revenue_records = self.load_revenue_records()
        self.schedules_records = self.load_schedules_records()
        self.maintenance_records = self.load_maintenance_records()

    def load_membership_records(self):
        data = read_csv(self.membership_csv)
        return [MembershipGrowth.from_dict(item) for item in data]

    def save_membership_records(self):
        data = [record.to_dict() for record in self.membership_records]
        write_csv(self.membership_csv, self.membership_fieldnames, data)

    def load_revenue_records(self):
        data = read_csv(self.revenue_csv)
        return [RevenueTrends.from_dict(item) for item in data]

    def save_revenue_records(self):
        data = [record.to_dict() for record in self.revenue_records]
        write_csv(self.revenue_csv, self.revenue_fieldnames, data)

    def load_schedules_records(self):
        data = read_csv(self.schedules_csv)
        return [TrainerSchedule.from_dict(item) for item in data]

    def save_schedules_records(self):
        data = [record.to_dict() for record in self.schedules_records]
        write_csv(self.schedules_csv, self.schedules_fieldnames, data)

    def load_maintenance_records(self):
        data = read_csv(self.maintenance_csv)
        return [EquipmentMaintenance.from_dict(item) for item in data]

    def save_maintenance_records(self):
        data = [record.to_dict() for record in self.maintenance_records]
        write_csv(self.maintenance_csv, self.maintenance_fieldnames, data)