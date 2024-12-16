# src/models/member.py

import random
import json
from datetime import datetime
from enum import Enum

class MembershipStatus(Enum):
    REGULAR = "Regular"
    PREMIUM = "Premium"
    TRIAL = "Trial"

class Member:
    def __init__(self, member_id, first_name, last_name, email, phone, membership_status, health_info=None):
        """
        Initializes a new member profile.
        :param member_id: Unique identifier for the member
        :param first_name: Member's first name
        :param last_name: Member's last name
        :param email: Member's email address
        :param phone: Member's phone number
        :param membership_status: Membership status (Regular, Premium, or Trial)
        :param health_info: Dictionary containing health details (optional)
        """
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.membership_status = membership_status
        self.health_info = health_info if health_info else {}
        self.appointments = []
        self.attendance = []

    def update_profile(self, first_name=None, last_name=None, email=None, phone=None):
        """
        Updates the member's profile information.
        :param first_name: New first name (optional)
        :param last_name: New last name (optional)
        :param email: New email (optional)
        :param phone: New phone number (optional)
        """
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
        if phone:
            self.phone = phone
        return self

    def update_health_info(self, health_info):
        """
        Updates the member's health information.
        :param health_info: New health information (dictionary)
        """
        self.health_info.update(health_info)
        return self

    def schedule_appointment(self, appointment):
        """
        Adds a new appointment for the member.
        :param appointment: Appointment object containing details about the appointment
        """
        self.appointments.append(appointment)
        return self

    def cancel_appointment(self, appointment_id):
        """
        Cancels an existing appointment.
        :param appointment_id: Unique appointment identifier
        """
        self.appointments = [appt for appt in self.appointments if appt.appointment_id != appointment_id]
        return self

    def mark_attendance(self, date_time=None):
        """
        Marks attendance for a member.
        :param date_time: Date and time when the member attended (optional)
        """
        date_time = date_time or datetime.now()
        self.attendance.append(date_time)
        return self

    def get_profile_info(self):
        """
        Retrieves member profile information as a dictionary.
        :return: Dictionary with member details
        """
        return {
            "member_id": self.member_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "membership_status": self.membership_status.value,
            "health_info": self.health_info,
            "appointments": [appt.get_appointment_info() for appt in self.appointments],
            "attendance": [str(att) for att in self.attendance]
        }

    @staticmethod
    def generate_member_id():
        """
        Generates a unique member ID (for simplicity, using a random integer).
        :return: Random unique member ID
        """
        return random.randint(100000, 999999)

    @staticmethod
    def from_json(json_data):
        """
        Creates a Member instance from a JSON object.
        :param json_data: JSON data representing a member
        :return: A Member instance
        """
        member_info = json.loads(json_data)
        member = Member(
            member_info['member_id'],
            member_info['first_name'],
            member_info['last_name'],
            member_info['email'],
            member_info['phone'],
            MembershipStatus[member_info['membership_status'].upper()],
            member_info['health_info']
        )
        return member

    def to_json(self):
        """
        Converts the member object to a JSON string.
        :return: JSON representation of the member
        """
        return json.dumps(self.get_profile_info())

class Appointment:
    def __init__(self, appointment_id, date_time, appointment_type, trainer_id=None):
        """
        Initializes a new appointment.
        :param appointment_id: Unique identifier for the appointment
        :param date_time: Date and time for the appointment
        :param appointment_type: Type of appointment (personal training, group class, etc.)
        :param trainer_id: ID of the trainer (optional)
        """
        self.appointment_id = appointment_id
        self.date_time = date_time
        self.appointment_type = appointment_type
        self.trainer_id = trainer_id

    def get_appointment_info(self):
        """
        Retrieves appointment details as a dictionary.
        :return: Dictionary with appointment details
        """
        return {
            "appointment_id": self.appointment_id,
            "date_time": str(self.date_time),
            "appointment_type": self.appointment_type,
            "trainer_id": self.trainer_id
        }

# Example usage:
if __name__ == "__main__":
    # Creating a new member
    member = Member(
        member_id=Member.generate_member_id(),
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone="123-456-7890",
        membership_status=MembershipStatus.REGULAR
    )

    # Update member profile
    member.update_profile(phone="987-654-3210")

    # Add health information
    member.update_health_info({"weight": 70, "height": 175})

    # Schedule an appointment
    appointment = Appointment(appointment_id=1001, date_time=datetime.now(), appointment_type="Personal Training")
    member.schedule_appointment(appointment)

    # Mark attendance
    member.mark_attendance()

    # Get member profile in JSON format
    print(member.to_json())
