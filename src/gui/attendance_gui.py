import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from src.attendance.attendance_manager import AttendanceManager
from src.attendance.attendance import Attendance

class AttendanceGUI:
    def __init__(self, root, attendance_manager):
        self.root = root
        self.attendance_manager = attendance_manager

        # Set theme and styles
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TLabel', background='#e0f7fa', font=('Helvetica', 10))
        style.configure('TFrame', background='#e0f7fa')
        style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6, relief="flat", background="#80deea")
        style.configure('Treeview', rowheight=25, font=('Helvetica', 10))
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.root.title("St Mary's Fitness - Attendance Tracking")
        self.root.geometry("1200x800")
        self.root.configure(bg="#e0f7fa")
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ttk.Label(self.root, text="Attendance Tracking",
                                     font=("Helvetica", 16, "bold"), background="#e0f7fa")
        self.title_label.grid(row=0, column=0, pady=10, sticky=tk.N)

        # Main Frame
        self.main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        self.main_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Labels and entries for Attendance
        self.id_label = ttk.Label(self.main_frame, text="Attendance ID:")
        self.id_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.id_entry = ttk.Entry(self.main_frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.member_id_label = ttk.Label(self.main_frame, text="Member ID:")
        self.member_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.member_id_entry = ttk.Entry(self.main_frame)
        self.member_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.class_name_label = ttk.Label(self.main_frame, text="Class Name:")
        self.class_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.class_name_entry = ttk.Entry(self.main_frame)
        self.class_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.check_in_label = ttk.Label(self.main_frame, text="Check-In (YYYY-MM-DD HH:MM:SS):")
        self.check_in_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.check_in_entry = ttk.Entry(self.main_frame)
        self.check_in_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.check_out_label = ttk.Label(self.main_frame, text="Check-Out (YYYY-MM-DD HH:MM:SS):")
        self.check_out_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.check_out_entry = ttk.Entry(self.main_frame)
        self.check_out_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons with styles for Attendance
        self.add_attendance_button = ttk.Button(self.main_frame, text="Add Attendance", command=self.add_attendance)
        self.add_attendance_button.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_attendance_button = ttk.Button(self.main_frame, text="Update Attendance", command=self.update_attendance)
        self.update_attendance_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_attendance_button = ttk.Button(self.main_frame, text="Delete Attendance", command=self.delete_attendance)
        self.delete_attendance_button.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_attendance_button = ttk.Button(self.main_frame, text="Load Attendance", command=self.load_attendance)
        self.load_attendance_button.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        # Report Buttons
        self.class_popularity_button = ttk.Button(self.main_frame, text="Class Popularity Report", command=self.show_class_popularity)
        self.class_popularity_button.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

        self.peak_hours_button = ttk.Button(self.main_frame, text="Peak Hours Report", command=self.show_peak_hours)
        self.peak_hours_button.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

        # Configure the main frame row/column weight for expandability
        for i in range(8):  # Assuming up to 8 rows in the frame
            self.main_frame.rowconfigure(i, weight=1)
        for j in range(2):  # Assuming 2 columns
            self.main_frame.columnconfigure(j, weight=1)

        # Frame for Treeview for Attendance
        self.tree_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.tree_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Treeview to display attendance records
        self.tree = ttk.Treeview(self.tree_frame, columns=('ID', 'Member ID', 'Class Name', 'Check-In', 'Check-Out'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Member ID', text='Member ID')
        self.tree.heading('Class Name', text='Class Name')
        self.tree.heading('Check-In', text='Check-In')
        self.tree.heading('Check-Out', text='Check-Out')
        self.tree.column('ID', width=50)
        self.tree.column('Member ID', width=100)
        self.tree.column('Class Name', width=150)
        self.tree.column('Check-In', width=150)
        self.tree.column('Check-Out', width=150)
        self.tree.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure column and row weights to make the layout expandable
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.tree_frame.columnconfigure(0, weight=1)
        self.tree_frame.rowconfigure(0, weight=1)

        self.load_attendance()

    def add_attendance(self):
        try:
            attendance = Attendance(
                id=int(self.id_entry.get()),
                member_id=int(self.member_id_entry.get()),
                class_name=self.class_name_entry.get(),
                check_in=datetime.strptime(self.check_in_entry.get(), '%Y-%m-%d %H:%M:%S'),
                check_out=datetime.strptime(self.check_out_entry.get(), '%Y-%m-%d %H:%M:%S')
            )
            self.attendance_manager.add_attendance_record(attendance)
            messagebox.showinfo("Success", "Attendance record added successfully.")
            self.load_attendance()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_attendance(self):
        try:
            attendance = Attendance(
                id=int(self.id_entry.get()),
                member_id=int(self.member_id_entry.get()),
                class_name=self.class_name_entry.get(),
                check_in=datetime.strptime(self.check_in_entry.get(), '%Y-%m-%d %H:%M:%S'),
                check_out=datetime.strptime(self.check_out_entry.get(), '%Y-%m-%d %H:%M:%S')
            )
            self.attendance_manager.update_attendance_record(attendance)
            messagebox.showinfo("Success", "Attendance record updated successfully.")
            self.load_attendance()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_attendance(self):
        try:
            selected_item = self.tree.selection()[0]
            attendance_id = int(self.tree.item(selected_item)['values'][0])
            self.attendance_manager.remove_attendance_record(attendance_id)
            messagebox.showinfo("Success", "Attendance record deleted successfully.")
            self.load_attendance()
        except IndexError:
            messagebox.showerror("Error", "No attendance record selected.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_attendance(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for record in self.attendance_manager.attendance_records:
            self.tree.insert('', tk.END, values=(record.id, record.member_id, record.class_name, record.check_in.strftime('%Y-%m-%d %H:%M:%S'), record.check_out.strftime('%Y-%m-%d %H:%M:%S')))

    def show_class_popularity(self):
        class_popularity = self.attendance_manager.get_class_popularity()
        report = "\n".join([f"{class_name}: {count} attendees" for class_name, count in class_popularity.items()])
        messagebox.showinfo("Class Popularity Report", report)

    def show_peak_hours(self):
        peak_hours = self.attendance_manager.get_peak_hours()
        report = "\n".join([f"{hour}:00 - {hour+1}:00: {count} attendees" for hour, count in enumerate(peak_hours)])
        messagebox.showinfo("Peak Hours Report", report)
