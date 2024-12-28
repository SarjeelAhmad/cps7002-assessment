import pytest
from datetime import datetime
from src.appointments.appointment_manager import AppointmentManager
from src.appointments.appointment import Appointment


@pytest.fixture
def appointment_manager():
    # Initialize the AppointmentManager with a test CSV file
    return AppointmentManager(csv_file="../data/appointments.csv")


def test_add_appointment(appointment_manager):
    appointment = Appointment(
        id=4,
        member_id=1004,
        trainer_id=2004,
        appointment_type="Nutrition Consultation",
        date_time=datetime.strptime("2024-12-23 14:00:00", "%Y-%m-%d %H:%M:%S"),
        status="Scheduled"
    )
    appointment_manager.add_appointment(appointment)


def test_remove_appointment(appointment_manager):
    appointment = Appointment(
        id=4,
        member_id=1004,
        trainer_id=2004,
        appointment_type="Nutrition Consultation",
        date_time=datetime.strptime("2024-12-23 14:00:00", "%Y-%m-%d %H:%M:%S"),
        status="Scheduled"
    )
    appointment_manager.add_appointment(appointment)
    appointment_manager.remove_appointment(4)


def test_update_appointment(appointment_manager):
    appointment = Appointment(
        id=4,
        member_id=1004,
        trainer_id=2004,
        appointment_type="Nutrition Consultation",
        date_time=datetime.strptime("2024-12-23 14:00:00", "%Y-%m-%d %H:%M:%S"),
        status="Scheduled"
    )
    appointment_manager.add_appointment(appointment)

    updated_appointment = Appointment(
        id=4,
        member_id=1004,
        trainer_id=2004,
        appointment_type="Nutrition Consultation",
        date_time=datetime.strptime("2024-12-23 16:00:00", "%Y-%m-%d %H:%M:%S"),
        status="Rescheduled"
    )
    appointment_manager.update_appointment(updated_appointment)


def test_load_appointments(appointment_manager):
    appointments = appointment_manager.load_appointments()
    assert len(appointments) == 3
    assert appointments[0].appointment_type == "Personal Training"
    assert appointments[1].appointment_type == "Group Class"
    assert appointments[2].appointment_type == "Consultation"


def test_save_appointments(appointment_manager):
    appointment = Appointment(
        id=4,
        member_id=1004,
        trainer_id=2004,
        appointment_type="Nutrition Consultation",
        date_time=datetime.strptime("2024-12-23 14:00:00", "%Y-%m-%d %H:%M:%S"),
        status="Scheduled"
    )
    appointment_manager.add_appointment(appointment)
    appointment_manager.save_appointments()
    appointments = appointment_manager.load_appointments()