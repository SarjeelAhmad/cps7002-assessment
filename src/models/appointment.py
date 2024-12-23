# src/models/appointment.py

from datetime import datetime

class Appointment:
    def __init__(self, appointment_id, member_id, trainer_id, date_time, appointment_type, status="Scheduled"):
        """
        Initializes a new Appointment instance.
        :param appointment_id: Unique identifier for the appointment
        :param member_id: Member ID who booked the appointment
        :param trainer_id: Trainer ID associated with the appointment
        :param date_time: Date and time of the appointment
        :param appointment_type: Type of appointment (e.g., personal training, group class)
        :param status: Status of the appointment (default: "Scheduled")
        """
        self.appointment_id = appointment_id
        self.member_id = member_id
        self.trainer_id = trainer_id
        self.date_time = date_time
        self.appointment_type = appointment_type
        self.status = status

    def cancel(self):
        """
        Cancels the appointment.
        """
        self.status = "Cancelled"

    def reschedule(self, new_date_time):
        """
        Reschedules the appointment to a new date and time.
        :param new_date_time: New date and time for the appointment
        """
        self.date_time = new_date_time

    def get_info(self):
        """
        Retrieves appointment details as a dictionary.
        :return: Dictionary with appointment details
        """
        return {
            "appointment_id": self.appointment_id,
            "member_id": self.member_id,
            "trainer_id": self.trainer_id,
            "date_time": str(self.date_time),
            "appointment_type": self.appointment_type,
            "status": self.status,
        }
