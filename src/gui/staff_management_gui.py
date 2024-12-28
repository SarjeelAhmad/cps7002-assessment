import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from src.staff_management.staff_manager import StaffManager
from src.staff_management.membership_growth import MembershipGrowth
from src.staff_management.revenue_trends import RevenueTrends
from src.staff_management.trainer_schedules import TrainerSchedule
from src.staff_management.equipment_maintenance import EquipmentMaintenance

class StaffManagementGUI:
    def __init__(self, root, staff_manager):
        self.root = root
        self.staff_manager = staff_manager

        # Set theme and styles
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TLabel', background='#e0f7fa', font=('Helvetica', 10))
        style.configure('TFrame', background='#e0f7fa')
        style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6, relief="flat", background="#80deea")
        style.configure('Treeview', rowheight=25, font=('Helvetica', 10))
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.root.title("St Mary's Fitness - Staff Management Dashboard")
        self.root.geometry("1200x800")
        self.root.configure(bg="#e0f7fa")
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ttk.Label(self.root, text="Staff Management Dashboard",
                                     font=("Helvetica", 16, "bold"), background="#e0f7fa")
        self.title_label.grid(row=0, column=0, columnspan=4, pady=10, sticky=tk.N)

        # Frames for different sections
        self.membership_frame = ttk.LabelFrame(self.root, text="Membership Growth", padding="10 10 10 10")
        self.membership_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.revenue_frame = ttk.LabelFrame(self.root, text="Revenue Trends", padding="10 10 10 10")
        self.revenue_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.schedules_frame = ttk.LabelFrame(self.root, text="Trainer Schedules", padding="10 10 10 10")
        self.schedules_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.maintenance_frame = ttk.LabelFrame(self.root, text="Equipment Maintenance", padding="10 10 10 10")
        self.maintenance_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.create_membership_widgets()
        self.create_revenue_widgets()
        self.create_schedules_widgets()
        self.create_maintenance_widgets()

        # Configure row and column weights for proper resizing
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

    def create_membership_widgets(self):
        # Membership Growth Widgets
        ttk.Label(self.membership_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.membership_id_entry = ttk.Entry(self.membership_frame)
        self.membership_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.membership_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.membership_date_entry = ttk.Entry(self.membership_frame)
        self.membership_date_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.membership_frame, text="New Members:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.membership_new_members_entry = ttk.Entry(self.membership_frame)
        self.membership_new_members_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.membership_frame, text="Total Members:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.membership_total_members_entry = ttk.Entry(self.membership_frame)
        self.membership_total_members_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons
        self.add_membership_button = ttk.Button(self.membership_frame, text="Add Record", command=self.add_membership_record)
        self.add_membership_button.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_membership_button = ttk.Button(self.membership_frame, text="Update Record", command=self.update_membership_record)
        self.update_membership_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_membership_button = ttk.Button(self.membership_frame, text="Delete Record", command=self.delete_membership_record)
        self.delete_membership_button.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_membership_button = ttk.Button(self.membership_frame, text="Load Records", command=self.load_membership_records)
        self.load_membership_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

    def create_revenue_widgets(self):
        # Revenue Trends Widgets
        ttk.Label(self.revenue_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.revenue_id_entry = ttk.Entry(self.revenue_frame)
        self.revenue_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.revenue_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.revenue_date_entry = ttk.Entry(self.revenue_frame)
        self.revenue_date_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.revenue_frame, text="Revenue:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.revenue_entry = ttk.Entry(self.revenue_frame)
        self.revenue_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons
        self.add_revenue_button = ttk.Button(self.revenue_frame, text="Add Record", command=self.add_revenue_record)
        self.add_revenue_button.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_revenue_button = ttk.Button(self.revenue_frame, text="Update Record", command=self.update_revenue_record)
        self.update_revenue_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_revenue_button = ttk.Button(self.revenue_frame, text="Delete Record", command=self.delete_revenue_record)
        self.delete_revenue_button.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_revenue_button = ttk.Button(self.revenue_frame, text="Load Records", command=self.load_revenue_records)
        self.load_revenue_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

    def create_schedules_widgets(self):
        # Trainer Schedules Widgets
        ttk.Label(self.schedules_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.schedules_id_entry = ttk.Entry(self.schedules_frame)
        self.schedules_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.schedules_frame, text="Trainer Name:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.schedules_trainer_name_entry = ttk.Entry(self.schedules_frame)
        self.schedules_trainer_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.schedules_frame, text="Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.schedules_date_entry = ttk.Entry(self.schedules_frame)
        self.schedules_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.schedules_frame, text="Class Name:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.schedules_class_name_entry = ttk.Entry(self.schedules_frame)
        self.schedules_class_name_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.schedules_frame, text="Start Time (HH:MM:SS):").grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.schedules_start_time_entry = ttk.Entry(self.schedules_frame)
        self.schedules_start_time_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.schedules_frame, text="End Time (HH:MM:SS):").grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.schedules_end_time_entry = ttk.Entry(self.schedules_frame)
        self.schedules_end_time_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons
        self.add_schedules_button = ttk.Button(self.schedules_frame, text="Add Record", command=self.add_schedules_record)
        self.add_schedules_button.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_schedules_button = ttk.Button(self.schedules_frame, text="Update Record", command=self.update_schedules_record)
        self.update_schedules_button.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_schedules_button = ttk.Button(self.schedules_frame, text="Delete Record", command=self.delete_schedules_record)
        self.delete_schedules_button.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_schedules_button = ttk.Button(self.schedules_frame, text="Load Records", command=self.load_schedules_records)
        self.load_schedules_button.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

    def create_maintenance_widgets(self):
        # Equipment Maintenance Widgets
        ttk.Label(self.maintenance_frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.maintenance_id_entry = ttk.Entry(self.maintenance_frame)
        self.maintenance_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.maintenance_frame, text="Equipment Name:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.maintenance_equipment_name_entry = ttk.Entry(self.maintenance_frame)
        self.maintenance_equipment_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.maintenance_frame, text="Last Maintenance (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.maintenance_last_entry = ttk.Entry(self.maintenance_frame)
        self.maintenance_last_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.maintenance_frame, text="Next Maintenance (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.maintenance_next_entry = ttk.Entry(self.maintenance_frame)
        self.maintenance_next_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(self.maintenance_frame, text="Status:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.maintenance_status_entry = ttk.Entry(self.maintenance_frame)
        self.maintenance_status_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons
        self.add_maintenance_button = ttk.Button(self.maintenance_frame, text="Add Record", command=self.add_maintenance_record)
        self.add_maintenance_button.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_maintenance_button = ttk.Button(self.maintenance_frame, text="Update Record", command=self.update_maintenance_record)
        self.update_maintenance_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_maintenance_button = ttk.Button(self.maintenance_frame, text="Delete Record", command=self.delete_maintenance_record)
        self.delete_maintenance_button.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_maintenance_button = ttk.Button(self.maintenance_frame, text="Load Records", command=self.load_maintenance_records)
        self.load_maintenance_button.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

    def add_membership_record(self):
        try:
            record = MembershipGrowth(
                id=int(self.membership_id_entry.get()),
                date=datetime.strptime(self.membership_date_entry.get(), '%Y-%m-%d'),
                new_members=int(self.membership_new_members_entry.get()),
                total_members=int(self.membership_total_members_entry.get())
            )
            self.staff_manager.membership_records.append(record)
            self.staff_manager.save_membership_records()
            messagebox.showinfo("Success", "Membership record added successfully.")
            self.load_membership_records()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_membership_record(self):
        try:
            record = MembershipGrowth(
                id=int(self.membership_id_entry.get()),
                date=datetime.strptime(self.membership_date_entry.get(), '%Y-%m-%d'),
                new_members=int(self.membership_new_members_entry.get()),
                total_members=int(self.membership_total_members_entry.get())
            )
            for i in range(len(self.staff_manager.membership_records)):
                if self.staff_manager.membership_records[i].id == record.id:
                    self.staff_manager.membership_records[i] = record
                    self.staff_manager.save_membership_records()
                    messagebox.showinfo("Success", "Membership record updated successfully.")
                    self.load_membership_records()
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_membership_record(self):
        try:
            record_id = int(self.membership_id_entry.get())
            self.staff_manager.membership_records = [record for record in self.staff_manager.membership_records if record.id != record_id]
            self.staff_manager.save_membership_records()
            messagebox.showinfo("Success", "Membership record deleted successfully.")
            self.load_membership_records()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_membership_records(self):
        for widget in self.membership_frame.winfo_children():
            widget.grid_forget()
        self.create_membership_widgets()
        for record in self.staff_manager.membership_records:
            print(record)

    def add_revenue_record(self):
        try:
            record = RevenueTrends(
                id=int(self.revenue_id_entry.get()),
                date=datetime.strptime(self.revenue_date_entry.get(), '%Y-%m-%d'),
                revenue=float(self.revenue_entry.get())
            )
            self.staff_manager.revenue_records.append(record)
            self.staff_manager.save_revenue_records()
            messagebox.showinfo("Success", "Revenue record added successfully.")
            self.load_revenue_records()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_revenue_record(self):
        try:
            record = RevenueTrends(
                id=int(self.revenue_id_entry.get()),
                date=datetime.strptime(self.revenue_date_entry.get(), '%Y-%m-%d'),
                revenue=float(self.revenue_entry.get())
            )
            for i in range(len(self.staff_manager.revenue_records)):
                if self.staff_manager.revenue_records[i].id == record.id:
                    self.staff_manager.revenue_records[i] = record
                    self.staff_manager.save_revenue_records()
                    messagebox.showinfo("Success", "Revenue record updated successfully.")
                    self.load_revenue_records()
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_revenue_record(self):
        try:
            record_id = int(self.revenue_id_entry.get())
            self.staff_manager.revenue_records = [record for record in self.staff_manager.revenue_records if record.id != record_id]
            self.staff_manager.save_revenue_records()
            messagebox.showinfo("Success", "Revenue record deleted successfully.")
            self.load_revenue_records()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_revenue_records(self):
        for widget in self.revenue_frame.winfo_children():
            widget.grid_forget()
        self.create_revenue_widgets()
        for record in self.staff_manager.revenue_records:
            print(record)

    def add_schedules_record(self):
        try:
            schedule = TrainerSchedule(
                id=int(self.schedules_id_entry.get()),
                trainer_name=self.schedules_trainer_name_entry.get(),
                date=datetime.strptime(self.schedules_date_entry.get(), '%Y-%m-%d'),
                class_name=self.schedules_class_name_entry.get(),
                start_time=datetime.strptime(self.schedules_start_time_entry.get(), '%H:%M:%S'),
                end_time=datetime.strptime(self.schedules_end_time_entry.get(), '%H:%M:%S')
            )
            self.staff_manager.schedules_records.append(schedule)
            self.staff_manager.save_schedules_records()
            messagebox.showinfo("Success", "Schedule record added successfully.")
            self.load_schedules_records()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_schedules_record(self):
        try:
            schedule = TrainerSchedule(
                id=int(self.schedules_id_entry.get()),
                trainer_name=self.schedules_trainer_name_entry.get(),
                date=datetime.strptime(self.schedules_date_entry.get(), '%Y-%m-%d'),
                class_name=self.schedules_class_name_entry.get(),
                start_time=datetime.strptime(self.schedules_start_time_entry.get(), '%H:%M:%S'),
                end_time=datetime.strptime(self.schedules_end_time_entry.get(), '%H:%M:%S')
            )
            for i, record in enumerate(self.staff_manager.schedules_records):
                if record.id == schedule.id:
                    self.staff_manager.schedules_records[i] = schedule
                    self.staff_manager.save_schedules_records()
                    messagebox.showinfo("Success", "Schedule record updated successfully.")
                    self.load_schedules_records()
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_schedules_record(self):
        try:
            selected_item = self.tree.selection()[0]
            schedule_id = int(self.tree.item(selected_item)['values'][0])
            self.staff_manager.schedules_records = [record for record in self.staff_manager.schedules_records if
                                                    record.id != schedule_id]
            self.staff_manager.save_schedules_records()
            messagebox.showinfo("Success", "Schedule record deleted successfully.")
            self.load_schedules_records()
        except IndexError:
            messagebox.showerror("Error", "No schedule record selected.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_schedules_records(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for record in self.staff_manager.schedules_records:
            self.tree.insert('', tk.END, values=(
            record.id, record.trainer_name, record.date.strftime('%Y-%m-%d'), record.class_name,
            record.start_time.strftime('%H:%M:%S'), record.end_time.strftime('%H:%M:%S')))

    def add_maintenance_record(self):
        try:
            maintenance = EquipmentMaintenance(
                id=int(self.maintenance_id_entry.get()),
                equipment_name=self.maintenance_equipment_name_entry.get(),
                last_maintenance=datetime.strptime(self.maintenance_last_entry.get(), '%Y-%m-%d'),
                next_maintenance=datetime.strptime(self.maintenance_next_entry.get(), '%Y-%m-%d'),
                status=self.maintenance_status_entry.get()
            )
            self.staff_manager.maintenance_records.append(maintenance)
            self.staff_manager.save_maintenance_records()
            messagebox.showinfo("Success", "Maintenance record added successfully.")
            self.load_maintenance_records()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_maintenance_record(self):
        try:
            maintenance = EquipmentMaintenance(
                id=int(self.maintenance_id_entry.get()),
                equipment_name=self.maintenance_equipment_name_entry.get(),
                last_maintenance=datetime.strptime(self.maintenance_last_entry.get(), '%Y-%m-%d'),
                next_maintenance=datetime.strptime(self.maintenance_next_entry.get(), '%Y-%m-%d'),
                status=self.maintenance_status_entry.get()
            )
            for i, record in enumerate(self.staff_manager.maintenance_records):
                if record.id == maintenance.id:
                    self.staff_manager.maintenance_records[i] = maintenance
                    self.staff_manager.save_maintenance_records()
                    messagebox.showinfo("Success", "Maintenance record updated successfully.")
                    self.load_maintenance_records()
                    break
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_maintenance_record(self):
        try:
            selected_item = self.tree.selection()[0]
            maintenance_id = int(self.tree.item(selected_item)['values'][0])
            self.staff_manager.maintenance_records = [record for record in self.staff_manager.maintenance_records if
                                                      record.id != maintenance_id]
            self.staff_manager.save_maintenance_records()
            messagebox.showinfo("Success", "Maintenance record deleted successfully.")
            self.load_maintenance_records()
        except IndexError:
            messagebox.showerror("Error", "No maintenance record selected.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_maintenance_records(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for record in self.staff_manager.maintenance_records:
            self.tree.insert('', tk.END, values=(
            record.id, record.equipment_name, record.last_maintenance.strftime('%Y-%m-%d'),
            record.next_maintenance.strftime('%Y-%m-%d'), record.status))