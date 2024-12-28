import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.workout_zones.workout_zone_manager import WorkoutZoneManager
from src.workout_zones.workout_zone import WorkoutZone

class WorkoutZonesGUI:
    def __init__(self, root, zone_manager):
        self.root = root
        self.zone_manager = zone_manager

        # Set theme and styles
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TLabel', background='#e0f7fa', font=('Helvetica', 10))
        style.configure('TFrame', background='#e0f7fa')
        style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6, relief="flat", background="#80deea")
        style.configure('Treeview', rowheight=25, font=('Helvetica', 10))
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.root.title("St Mary's Fitness - Workout Zones")
        self.root.configure(bg="#e0f7fa")
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ttk.Label(self.root, text="Workout Zones Management",
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

        self.name_label = ttk.Label(self.main_frame, text="Name:")
        self.name_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.name_entry = ttk.Entry(self.main_frame)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.exercise_types_label = ttk.Label(self.main_frame, text="Exercise Types:")
        self.exercise_types_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.exercise_types_entry = ttk.Entry(self.main_frame)
        self.exercise_types_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.attendant_name_label = ttk.Label(self.main_frame, text="Attendant Name:")
        self.attendant_name_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.attendant_name_entry = ttk.Entry(self.main_frame)
        self.attendant_name_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.updates_label = ttk.Label(self.main_frame, text="Updates:")
        self.updates_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.updates_entry = ttk.Entry(self.main_frame)
        self.updates_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.class_schedule_label = ttk.Label(self.main_frame, text="Class Schedule:")
        self.class_schedule_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.class_schedule_entry = ttk.Entry(self.main_frame)
        self.class_schedule_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.promotions_label = ttk.Label(self.main_frame, text="Promotions:")
        self.promotions_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
        self.promotions_entry = ttk.Entry(self.main_frame)
        self.promotions_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons with styles
        self.add_button = ttk.Button(self.main_frame, text="Add Zone", command=self.add_zone)
        self.add_button.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_button = ttk.Button(self.main_frame, text="Update Zone", command=self.update_zone)
        self.update_button.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_button = ttk.Button(self.main_frame, text="Delete Zone", command=self.delete_zone)
        self.delete_button.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_button = ttk.Button(self.main_frame, text="Load Zones", command=self.load_zones)
        self.load_button.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W)

        # Configure the main frame row/column weight for expandability
        for i in range(9):  # Assuming up to 9 rows in the frame
            self.main_frame.rowconfigure(i, weight=1)
        for j in range(2):  # Assuming 2 columns
            self.main_frame.columnconfigure(j, weight=1)

        # Frame for Treeview
        self.tree_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.tree_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Treeview to display zones
        self.tree = ttk.Treeview(self.tree_frame, columns=('ID', 'Name', 'Exercise Types', 'Attendant', 'Updates', 'Class Schedule', 'Promotions'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Exercise Types', text='Exercise Types')
        self.tree.heading('Attendant', text='Attendant')
        self.tree.heading('Updates', text='Updates')
        self.tree.heading('Class Schedule', text='Class Schedule')
        self.tree.heading('Promotions', text='Promotions')
        self.tree.column('ID', width=50)
        self.tree.column('Name', width=100)
        self.tree.column('Exercise Types', width=200)
        self.tree.column('Attendant', width=100)
        self.tree.column('Updates', width=200)
        self.tree.column('Class Schedule', width=200)
        self.tree.column('Promotions', width=200)
        self.tree.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure column and row weights to make the layout expandable
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.tree_frame.columnconfigure(0, weight=1)
        self.tree_frame.rowconfigure(0, weight=1)

        self.load_zones()

    def add_zone(self):
        try:
            zone = WorkoutZone(
                id=int(self.id_entry.get()),
                name=self.name_entry.get(),
                exercise_types=self.exercise_types_entry.get(),
                attendant_name=self.attendant_name_entry.get(),
                updates=self.updates_entry.get(),
                class_schedule=self.class_schedule_entry.get(),
                promotions=self.promotions_entry.get()
            )
            self.zone_manager.add_workout_zone(zone)
            messagebox.showinfo("Success", "Zone added successfully.")
            self.load_zones()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_zone(self):
        try:
            zone = WorkoutZone(
                id=int(self.id_entry.get()),
                name=self.name_entry.get(),
                exercise_types=self.exercise_types_entry.get(),
                attendant_name=self.attendant_name_entry.get(),
                updates=self.updates_entry.get(),
                class_schedule=self.class_schedule_entry.get(),
                promotions=self.promotions_entry.get()
            )
            self.zone_manager.update_workout_zone(zone)
            messagebox.showinfo("Success", "Zone updated successfully.")
            self.load_zones()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_zone(self):
        try:
            selected_item = self.tree.selection()[0]
            zone_id = int(self.tree.item(selected_item)['values'][0])
            self.zone_manager.remove_workout_zone(zone_id)
            messagebox.showinfo("Success", "Zone deleted successfully.")
            self.load_zones()
        except IndexError:
            messagebox.showerror("Error", "No zone selected.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_zones(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for zone in self.zone_manager.workout_zones:
            self.tree.insert('', tk.END, values=(zone.id, zone.name, zone.exercise_types, zone.attendant_name, zone.updates, zone.class_schedule, zone.promotions))

