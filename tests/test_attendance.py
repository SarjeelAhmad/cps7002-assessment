import pytest
from datetime import datetime
from src.attendance.attendance_manager import AttendanceManager
from src.attendance.attendance import Attendance


@pytest.fixture
def attendance_manager():
    # Initialize the AttendanceManager with a test CSV file
    return AttendanceManager(csv_file="../data/attendance.csv")


def test_add_attendance_record(attendance_manager):
    record = Attendance(
        id=6,
        member_id=1006,
        class_name="Crossfit",
        check_in=datetime.strptime("2024-12-15 14:00:00", "%Y-%m-%d %H:%M:%S"),
        check_out=datetime.strptime("2024-12-15 15:00:00", "%Y-%m-%d %H:%M:%S")
    )
    attendance_manager.add_attendance_record(record)


def test_remove_attendance_record(attendance_manager):
    record = Attendance(
        id=6,
        member_id=1006,
        class_name="Crossfit",
        check_in=datetime.strptime("2024-12-15 14:00:00", "%Y-%m-%d %H:%M:%S"),
        check_out=datetime.strptime("2024-12-15 15:00:00", "%Y-%m-%d %H:%M:%S")
    )
    attendance_manager.add_attendance_record(record)
    attendance_manager.remove_attendance_record(6)


def test_update_attendance_record(attendance_manager):
    record = Attendance(
        id=6,
        member_id=1006,
        class_name="Crossfit",
        check_in=datetime.strptime("2024-12-15 14:00:00", "%Y-%m-%d %H:%M:%S"),
        check_out=datetime.strptime("2024-12-15 15:00:00", "%Y-%m-%d %H:%M:%S")
    )
    attendance_manager.add_attendance_record(record)

    updated_record = Attendance(
        id=6,
        member_id=1006,
        class_name="Crossfit",
        check_in=datetime.strptime("2024-12-15 14:30:00", "%Y-%m-%d %H:%M:%S"),
        check_out=datetime.strptime("2024-12-15 15:30:00", "%Y-%m-%d %H:%M:%S")
    )
    attendance_manager.update_attendance_record(updated_record)


def test_load_attendance_records(attendance_manager):
    records = attendance_manager.load_attendance_records()


def test_save_attendance_records(attendance_manager):
    record = Attendance(
        id=6,
        member_id=1006,
        class_name="Crossfit",
        check_in=datetime.strptime("2024-12-15 14:00:00", "%Y-%m-%d %H:%M:%S"),
        check_out=datetime.strptime("2024-12-15 15:00:00", "%Y-%m-%d %H:%M:%S")
    )
    attendance_manager.add_attendance_record(record)
    attendance_manager.save_attendance_records()
    records = attendance_manager.load_attendance_records()