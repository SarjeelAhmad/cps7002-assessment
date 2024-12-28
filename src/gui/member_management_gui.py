import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.member_management.member_manager import MemberManager
from src.member_management.gym_location import GymLocation

class MemberManagementGUI:
    def __init__(self, root, member_manager):
        self.root = root
        self.member_manager = member_manager

        # Set theme and styles
        style = ttk.Style()
        style.theme_use("clam")  # Use a modern theme
        style.configure('TLabel', background='#e0f7fa', font=('Helvetica', 10))
        style.configure('TFrame', background='#e0f7fa')
        style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6, relief="flat", background="#80deea")
        style.configure('Treeview', rowheight=25, font=('Helvetica', 10))
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.root.title("St Mary's Fitness")
        self.root.configure(bg="#e0f7fa")  # Set background color
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ttk.Label(self.root, text="St Mary's Fitness Management System",
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

        self.city_label = ttk.Label(self.main_frame, text="City:")
        self.city_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.city_entry = ttk.Entry(self.main_frame)
        self.city_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.address_label = ttk.Label(self.main_frame, text="Address:")
        self.address_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.address_entry = ttk.Entry(self.main_frame)
        self.address_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.manager_name_label = ttk.Label(self.main_frame, text="Manager Name:")
        self.manager_name_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.manager_name_entry = ttk.Entry(self.main_frame)
        self.manager_name_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.workout_zones_label = ttk.Label(self.main_frame, text="Workout Zones:")
        self.workout_zones_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.workout_zones_entry = ttk.Entry(self.main_frame)
        self.workout_zones_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons with styles
        self.add_button = ttk.Button(self.main_frame, text="Add Location", command=self.add_location)
        self.add_button.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_button = ttk.Button(self.main_frame, text="Update Location", command=self.update_location)
        self.update_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_button = ttk.Button(self.main_frame, text="Delete Location", command=self.delete_location)
        self.delete_button.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_button = ttk.Button(self.main_frame, text="Load Locations", command=self.load_locations)
        self.load_button.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        # Configure the main frame row/column weight for expandability
        for i in range(7):  # Assuming up to 7 rows in the frame
            self.main_frame.rowconfigure(i, weight=1)
        for j in range(2):  # Assuming 2 columns
            self.main_frame.columnconfigure(j, weight=1)

        # Frame for Treeview
        self.tree_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.tree_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Treeview to display locations
        self.tree = ttk.Treeview(self.tree_frame, columns=('ID', 'City', 'Address', 'Manager', 'Workout Zones'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('City', text='City')
        self.tree.heading('Address', text='Address')
        self.tree.heading('Manager', text='Manager')
        self.tree.heading('Workout Zones', text='Workout Zones')
        self.tree.column('ID', width=50)
        self.tree.column('City', width=100)
        self.tree.column('Address', width=200)
        self.tree.column('Manager', width=100)
        self.tree.column('Workout Zones', width=200)
        self.tree.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure column and row weights to make the layout expandable
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.tree_frame.columnconfigure(0, weight=1)
        self.tree_frame.rowconfigure(0, weight=1)

        self.load_locations()

    def add_location(self):
        try:
            location = GymLocation(
                id=int(self.id_entry.get()),
                city=self.city_entry.get(),
                address=self.address_entry.get(),
                manager_name=self.manager_name_entry.get(),
                workout_zones=self.workout_zones_entry.get()
            )
            self.member_manager.add_location(location)
            messagebox.showinfo("Success", "Location added successfully.")
            self.load_locations()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_location(self):
        try:
            location = GymLocation(
                id=int(self.id_entry.get()),
                city=self.city_entry.get(),
                address=self.address_entry.get(),
                manager_name=self.manager_name_entry.get(),
                workout_zones=self.workout_zones_entry.get()
            )
            self.member_manager.update_location(location)
            messagebox.showinfo("Success", "Location updated successfully.")
            self.load_locations()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_location(self):
        try:
            selected_item = self.tree.selection()[0]
            location_id = int(self.tree.item(selected_item)['values'][0])
            self.member_manager.remove_location(location_id)
            messagebox.showinfo("Success", "Location deleted successfully.")
            self.load_locations()
        except IndexError:
            messagebox.showerror("Error", "No location selected.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_locations(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for location in self.member_manager.locations:
            self.tree.insert('', tk.END, values=(location.id, location.city, location.address, location.manager_name, location.workout_zones))
