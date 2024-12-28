import tkinter as tk
from tkinter import ttk
from src.member_management.member_manager import MemberManager
from src.gui.member_management_gui import MemberManagementGUI
from src.workout_zones.workout_zone_manager import WorkoutZoneManager
from src.gui.workout_zones_gui import WorkoutZonesGUI
from src.member_profiles.member_profile_manager import MemberProfileManager
from src.gui.member_profiles_gui import MemberProfilesGUI
from src.appointments.appointment_manager import AppointmentManager
from src.gui.appointments_gui import AppointmentsGUI
from src.payments.payment_manager import PaymentManager
from src.gui.payments_gui import PaymentsGUI
from src.attendance.attendance_manager import AttendanceManager
from src.gui.attendance_gui import AttendanceGUI
from src.staff_management.staff_manager import StaffManager
from src.gui.staff_management_gui import StaffManagementGUI

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("St Mary's Fitness Management System")
        self.root.geometry("1000x600")

        # Set theme and styles
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TLabel', background='#e0f7fa', font=('Helvetica', 10))
        style.configure('TFrame', background='#e0f7fa')
        style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6, relief="flat", background="#80deea")
        style.configure('Treeview', rowheight=25, font=('Helvetica', 10))
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.root.configure(bg="#e0f7fa")

        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ttk.Label(self.root, text="St Mary's Fitness Management System",
                                     font=("Helvetica", 16, "bold"), background="#e0f7fa")
        self.title_label.pack(pady=10)

        # Frame for buttons
        self.button_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.button_frame.pack(pady=20)

        # Buttons for different management systems
        self.member_button = ttk.Button(self.button_frame, text="Manage Members", command=self.open_member_management)
        self.member_button.grid(row=0, column=0, padx=10, pady=10)

        self.zone_button = ttk.Button(self.button_frame, text="Manage Workout Zones",
                                      command=self.open_workout_zones_management)
        self.zone_button.grid(row=0, column=1, padx=10, pady=10)

        self.profile_button = ttk.Button(self.button_frame, text="Manage Member Profiles",
                                         command=self.open_member_profiles_management)
        self.profile_button.grid(row=0, column=2, padx=10, pady=10)

        self.appointment_button = ttk.Button(self.button_frame, text="Manage Appointments",
                                             command=self.open_appointments_management)
        self.appointment_button.grid(row=0, column=3, padx=10, pady=10)

        self.payment_button = ttk.Button(self.button_frame, text="Manage Payments",
                                         command=self.open_payments_management)
        self.payment_button.grid(row=1, column=0, padx=10, pady=10)

        self.attendance_button = ttk.Button(self.button_frame, text="Manage Attendance",
                                            command=self.open_attendance_management)
        self.attendance_button.grid(row=1, column=1, padx=10, pady=10)

        self.staff_button = ttk.Button(self.button_frame, text="Staff Management Dashboard",
                                       command=self.open_staff_management)
        self.staff_button.grid(row=1, column=2, padx=10, pady=10)

    def open_member_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.geometry("800x600")
        member_manager = MemberManager(csv_file="../data/gym_locations.csv")
        MemberManagementGUI(self.new_window, member_manager)

    def open_workout_zones_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.geometry("1000x600")
        zone_manager = WorkoutZoneManager(csv_file="../data/workout_zones.csv")
        WorkoutZonesGUI(self.new_window, zone_manager)

    def open_member_profiles_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.geometry("1000x600")
        profile_manager = MemberProfileManager(csv_file="../data/member_profiles.csv")
        MemberProfilesGUI(self.new_window, profile_manager)

    def open_appointments_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.geometry("1200x600")
        appointment_manager = AppointmentManager(csv_file="../data/appointments.csv")
        AppointmentsGUI(self.new_window, appointment_manager)

    def open_payments_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.geometry("1200x600")
        payment_manager = PaymentManager(payments_csv_file="../data/payments.csv",
                                         subscriptions_csv_file="../data/subscriptions.csv")
        PaymentsGUI(self.new_window, payment_manager)

    def open_attendance_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.geometry("1200x800")
        attendance_manager = AttendanceManager(csv_file="../data/attendance.csv")
        AttendanceGUI(self.new_window, attendance_manager)

    def open_staff_management(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.geometry("1200x800")
        staff_manager = StaffManager(membership_csv="../data/membership_growth.csv", revenue_csv="../data/revenue_trends.csv",
                                     schedules_csv="../data/trainers_schedule.csv", maintenance_csv="../data/equipment_maintenance.csv")
        StaffManagementGUI(self.new_window, staff_manager)

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()