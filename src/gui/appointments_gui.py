import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime
from src.appointments.appointment_manager import AppointmentManager
from src.appointments.appointment import Appointment

class AppointmentsGUI:
    def __init__(self, root, appointment_manager):
        self.root = root
        self.appointment_manager = appointment_manager

        # Set theme and styles
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TLabel', background='#e0f7fa', font=('Helvetica', 10))
        style.configure('TFrame', background='#e0f7fa')
        style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6, relief="flat", background="#80deea")
        style.configure('Treeview', rowheight=25, font=('Helvetica', 10))
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.root.title("St Mary's Fitness - Appointments")
        self.root.configure(bg="#e0f7fa")
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ttk.Label(self.root, text="Appointments Management",
                                     font=("Helvetica", 16, "bold"), background="#e0f7fa")
        self.title_label.grid(row=0, column=0, pady=10, sticky=tk.N)

        # Main Frame
        self.main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        self.main_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Labels and entries
        self.id_label = ttk.Label(self.main_frame, text="ID:")
        self.id_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.id_entry = ttk.Entry(self.main_frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.member_id_label = ttk.Label(self.main_frame, text="Member ID:")
        self.member_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.member_id_entry = ttk.Entry(self.main_frame)
        self.member_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.trainer_id_label = ttk.Label(self.main_frame, text="Trainer ID:")
        self.trainer_id_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.trainer_id_entry = ttk.Entry(self.main_frame)
        self.trainer_id_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.appointment_type_label = ttk.Label(self.main_frame, text="Appointment Type:")
        self.appointment_type_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.appointment_type_entry = ttk.Entry(self.main_frame)
        self.appointment_type_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.date_time_label = ttk.Label(self.main_frame, text="Date & Time (YYYY-MM-DD HH:MM:SS):")
        self.date_time_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.date_time_entry = ttk.Entry(self.main_frame)
        self.date_time_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.status_label = ttk.Label(self.main_frame, text="Status:")
        self.status_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.status_entry = ttk.Entry(self.main_frame)
        self.status_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons with styles
        self.add_button = ttk.Button(self.main_frame, text="Add Appointment", command=self.add_appointment)
        self.add_button.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_button = ttk.Button(self.main_frame, text="Update Appointment", command=self.update_appointment)
        self.update_button.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_button = ttk.Button(self.main_frame, text="Delete Appointment", command=self.delete_appointment)
        self.delete_button.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_button = ttk.Button(self.main_frame, text="Load Appointments", command=self.load_appointments)
        self.load_button.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

        # Configure the main frame row/column weight for expandability
        for i in range(8):  # Assuming up to 8 rows in the frame
            self.main_frame.rowconfigure(i, weight=1)
        for j in range(2):  # Assuming 2 columns
            self.main_frame.columnconfigure(j, weight=1)

        # Frame for Treeview
        self.tree_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.tree_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Treeview to display appointments
        self.tree = ttk.Treeview(self.tree_frame, columns=('ID', 'Member ID', 'Trainer ID', 'Appointment Type', 'Date & Time', 'Status'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Member ID', text='Member ID')
        self.tree.heading('Trainer ID', text='Trainer ID')
        self.tree.heading('Appointment Type', text='Appointment Type')
        self.tree.heading('Date & Time', text='Date & Time')
        self.tree.heading('Status', text='Status')
        self.tree.column('ID', width=50)
        self.tree.column('Member ID', width=100)
        self.tree.column('Trainer ID', width=100)
        self.tree.column('Appointment Type', width=150)
        self.tree.column('Date & Time', width=200)
        self.tree.column('Status', width=100)
        self.tree.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure column and row weights to make the layout expandable
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.tree_frame.columnconfigure(0, weight=1)
        self.tree_frame.rowconfigure(0, weight=1)

        self.load_appointments()

    def add_appointment(self):
        try:
            appointment = Appointment(
                id=int(self.id_entry.get()),
                member_id=int(self.member_id_entry.get()),
                trainer_id=int(self.trainer_id_entry.get()),
                appointment_type=self.appointment_type_entry.get(),
                date_time=datetime.strptime(self.date_time_entry.get(), '%Y-%m-%d %H:%M:%S'),
                status=self.status_entry.get()
            )
            self.appointment_manager.add_appointment(appointment)
            messagebox.showinfo("Success", "Appointment added successfully.")
            self.load_appointments()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_appointment(self):
        try:
            appointment = Appointment(
                id=int(self.id_entry.get()),
                member_id=int(self.member_id_entry.get()),
                trainer_id=int(self.trainer_id_entry.get()),
                appointment_type=self.appointment_type_entry.get(),
                date_time=datetime.strptime(self.date_time_entry.get(), '%Y-%m-%d %H:%M:%S'),
                status=self.status_entry.get()
            )
            self.appointment_manager.update_appointment(appointment)
            messagebox.showinfo("Success", "Appointment updated successfully.")
            self.load_appointments()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_appointment(self):
        try:
            selected_item = self.tree.selection()[0]
            appointment_id = int(self.tree.item(selected_item)['values'][0])
            self.appointment_manager.remove_appointment(appointment_id)
            messagebox.showinfo("Success", "Appointment deleted successfully.")
            self.load_appointments()
        except IndexError:
            messagebox.showerror("Error", "No appointment selected.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_appointments(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for appointment in self.appointment_manager.appointments:
            self.tree.insert('', tk.END, values=(appointment.id, appointment.member_id, appointment.trainer_id, appointment.appointment_type, appointment.date_time.strftime('%Y-%m-%d %H:%M:%S'), appointment.status))
