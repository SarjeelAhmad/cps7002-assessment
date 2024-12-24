from src.database.csv_handler import read_csv, write_csv
from src.attendance.attendance import Attendance

class AttendanceManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fieldnames = ['id', 'member_id', 'class_name', 'check_in', 'check_out']
        self.attendance_records = self.load_attendance_records()

    def load_attendance_records(self):
        data = read_csv(self.csv_file)
        return [Attendance.from_dict(item) for item in data]

    def save_attendance_records(self):
        data = [record.to_dict() for record in self.attendance_records]
        write_csv(self.csv_file, self.fieldnames, data)

    def add_attendance_record(self, record):
        self.attendance_records.append(record)
        self.save_attendance_records()

    def remove_attendance_record(self, record_id):
        self.attendance_records = [record for record in self.attendance_records if record.id != record_id]
        self.save_attendance_records()

    def update_attendance_record(self, updated_record):
        for i, record in enumerate(self.attendance_records):
            if record.id == updated_record.id:
                self.attendance_records[i] = updated_record
                self.save_attendance_records()
                break

    def get_class_popularity(self):
        class_popularity = {}
        for record in self.attendance_records:
            if record.class_name not in class_popularity:
                class_popularity[record.class_name] = 0
            class_popularity[record.class_name] += 1
        return class_popularity

    def get_peak_hours(self):
        hours = [0] * 24
        for record in self.attendance_records:
            check_in_hour = record.check_in.hour
            check_out_hour = record.check_out.hour
            for hour in range(check_in_hour, check_out_hour + 1):
                hours[hour] += 1
        return hours