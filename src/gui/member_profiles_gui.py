import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.member_profiles.member_profile_manager import MemberProfileManager
from src.member_profiles.member_profile import MemberProfile

class MemberProfilesGUI:
    def __init__(self, root, profile_manager):
        self.root = root
        self.profile_manager = profile_manager

        # Set theme and styles
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TLabel', background='#e0f7fa', font=('Helvetica', 10))
        style.configure('TFrame', background='#e0f7fa')
        style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6, relief="flat", background="#80deea")
        style.configure('Treeview', rowheight=25, font=('Helvetica', 10))
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.root.title("St Mary's Fitness - Member Profiles")
        self.root.configure(bg="#e0f7fa")
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ttk.Label(self.root, text="Member Profiles Management",
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

        self.age_label = ttk.Label(self.main_frame, text="Age:")
        self.age_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.age_entry = ttk.Entry(self.main_frame)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.gender_label = ttk.Label(self.main_frame, text="Gender:")
        self.gender_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.gender_entry = ttk.Entry(self.main_frame)
        self.gender_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.membership_type_label = ttk.Label(self.main_frame, text="Membership Type:")
        self.membership_type_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.membership_type_entry = ttk.Entry(self.main_frame)
        self.membership_type_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.health_info_label = ttk.Label(self.main_frame, text="Health Info:")
        self.health_info_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.health_info_entry = ttk.Entry(self.main_frame)
        self.health_info_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.membership_status_label = ttk.Label(self.main_frame, text="Membership Status:")
        self.membership_status_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
        self.membership_status_entry = ttk.Entry(self.main_frame)
        self.membership_status_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons with styles
        self.add_button = ttk.Button(self.main_frame, text="Add Member", command=self.add_member)
        self.add_button.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_button = ttk.Button(self.main_frame, text="Update Member", command=self.update_member)
        self.update_button.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_button = ttk.Button(self.main_frame, text="Delete Member", command=self.delete_member)
        self.delete_button.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_button = ttk.Button(self.main_frame, text="Load Members", command=self.load_members)
        self.load_button.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W)

        # Configure the main frame row/column weight for expandability
        for i in range(9):  # Assuming up to 9 rows in the frame
            self.main_frame.rowconfigure(i, weight=1)
        for j in range(2):  # Assuming 2 columns
            self.main_frame.columnconfigure(j, weight=1)

        # Frame for Treeview
        self.tree_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.tree_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Treeview to display members
        self.tree = ttk.Treeview(self.tree_frame, columns=('ID', 'Name', 'Age', 'Gender', 'Membership Type', 'Health Info', 'Membership Status'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Age', text='Age')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('Membership Type', text='Membership Type')
        self.tree.heading('Health Info', text='Health Info')
        self.tree.heading('Membership Status', text='Membership Status')
        self.tree.column('ID', width=50)
        self.tree.column('Name', width=100)
        self.tree.column('Age', width=50)
        self.tree.column('Gender', width=80)
        self.tree.column('Membership Type', width=100)
        self.tree.column('Health Info', width=200)
        self.tree.column('Membership Status', width=100)
        self.tree.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure column and row weights to make the layout expandable
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.tree_frame.columnconfigure(0, weight=1)
        self.tree_frame.rowconfigure(0, weight=1)

        self.load_members()

    def add_member(self):
        try:
            member = MemberProfile(
                id=int(self.id_entry.get()),
                name=self.name_entry.get(),
                age=int(self.age_entry.get()),
                gender=self.gender_entry.get(),
                membership_type=self.membership_type_entry.get(),
                health_info=self.health_info_entry.get(),
                membership_status=self.membership_status_entry.get()
            )
            self.profile_manager.add_member_profile(member)
            messagebox.showinfo("Success", "Member added successfully.")
            self.load_members()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_member(self):
        try:
            member = MemberProfile(
                id=int(self.id_entry.get()),
                name=self.name_entry.get(),
                age=int(self.age_entry.get()),
                gender=self.gender_entry.get(),
                membership_type=self.membership_type_entry.get(),
                health_info=self.health_info_entry.get(),
                membership_status=self.membership_status_entry.get()
            )
            self.profile_manager.update_member_profile(member)
            messagebox.showinfo("Success", "Member updated successfully.")
            self.load_members()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_member(self):
        try:
            selected_item = self.tree.selection()[0]
            member_id = int(self.tree.item(selected_item)['values'][0])
            self.profile_manager.remove_member_profile(member_id)
            messagebox.showinfo("Success", "Member deleted successfully.")
            self.load_members()
        except IndexError:
            messagebox.showerror("Error", "No member selected.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_members(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for member in self.profile_manager.member_profiles:
            self.tree.insert('', tk.END, values=(member.id, member.name, member.age, member.gender, member.membership_type, member.health_info, member.membership_status))

