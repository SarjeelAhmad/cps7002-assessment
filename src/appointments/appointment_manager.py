from src.database.csv_handler import read_csv, write_csv
from src.appointments.appointment import Appointment

class AppointmentManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.fieldnames = ['id', 'member_id', 'trainer_id', 'appointment_type', 'date_time', 'status']
        self.appointments = self.load_appointments()

    def load_appointments(self):
        data = read_csv(self.csv_file)
        return [Appointment.from_dict(item) for item in data]

    def save_appointments(self):
        data = [appointment.to_dict() for appointment in self.appointments]
        write_csv(self.csv_file, self.fieldnames, data)

    def add_appointment(self, appointment):
        self.appointments.append(appointment)
        self.save_appointments()

    def remove_appointment(self, appointment_id):
        self.appointments = [appointment for appointment in self.appointments if appointment.id != appointment_id]
        self.save_appointments()

    def update_appointment(self, updated_appointment):
        for i, appointment in enumerate(self.appointments):
            if appointment.id == updated_appointment.id:
                self.appointments[i] = updated_appointment
                self.save_appointments()
                break