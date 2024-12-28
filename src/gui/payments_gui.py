import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from src.payments.payment_manager import PaymentManager
from src.payments.payment import Payment
from src.payments.subscription import Subscription

class PaymentsGUI:
    def __init__(self, root, payment_manager):
        self.root = root
        self.payment_manager = payment_manager

        # Set theme and styles
        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TLabel', background='#e0f7fa', font=('Helvetica', 10))
        style.configure('TFrame', background='#e0f7fa')
        style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=6, relief="flat", background="#80deea")
        style.configure('Treeview', rowheight=25, font=('Helvetica', 10))
        style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.root.title("St Mary's Fitness - Payments and Subscriptions")
        self.root.geometry("1200x800")  # Set the window geometry
        self.root.configure(bg="#e0f7fa")
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = ttk.Label(self.root, text="Payments and Subscriptions Management",
                                     font=("Helvetica", 16, "bold"), background="#e0f7fa")
        self.title_label.grid(row=0, column=0, pady=10, sticky=tk.N)

        # Main Frame
        self.main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        self.main_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Labels and entries for Payments
        self.id_label = ttk.Label(self.main_frame, text="Payment ID:")
        self.id_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.id_entry = ttk.Entry(self.main_frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.member_id_label = ttk.Label(self.main_frame, text="Member ID:")
        self.member_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.member_id_entry = ttk.Entry(self.main_frame)
        self.member_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.amount_label = ttk.Label(self.main_frame, text="Amount:")
        self.amount_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.amount_entry = ttk.Entry(self.main_frame)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.date_label = ttk.Label(self.main_frame, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.date_entry = ttk.Entry(self.main_frame)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.payment_method_label = ttk.Label(self.main_frame, text="Payment Method:")
        self.payment_method_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.payment_method_entry = ttk.Entry(self.main_frame)
        self.payment_method_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.description_label = ttk.Label(self.main_frame, text="Description:")
        self.description_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.description_entry = ttk.Entry(self.main_frame)
        self.description_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.status_label = ttk.Label(self.main_frame, text="Status:")
        self.status_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
        self.status_entry = ttk.Entry(self.main_frame)
        self.status_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons with styles for Payments
        self.add_payment_button = ttk.Button(self.main_frame, text="Add Payment", command=self.add_payment)
        self.add_payment_button.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_payment_button = ttk.Button(self.main_frame, text="Update Payment", command=self.update_payment)
        self.update_payment_button.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_payment_button = ttk.Button(self.main_frame, text="Delete Payment", command=self.delete_payment)
        self.delete_payment_button.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_payment_button = ttk.Button(self.main_frame, text="Load Payments", command=self.load_payments)
        self.load_payment_button.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W)

        # Configure the main frame row/column weight for expandability
        for i in range(9):  # Assuming up to 9 rows in the frame
            self.main_frame.rowconfigure(i, weight=1)
        for j in range(2):  # Assuming 2 columns
            self.main_frame.columnconfigure(j, weight=1)

        # Frame for Treeview for Payments
        self.tree_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.tree_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Treeview to display payments
        self.tree = ttk.Treeview(self.tree_frame, columns=('ID', 'Member ID', 'Amount', 'Date', 'Payment Method', 'Description', 'Status'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Member ID', text='Member ID')
        self.tree.heading('Amount', text='Amount')
        self.tree.heading('Date', text='Date')
        self.tree.heading('Payment Method', text='Payment Method')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Status', text='Status')
        self.tree.column('ID', width=50)
        self.tree.column('Member ID', width=100)
        self.tree.column('Amount', width=100)
        self.tree.column('Date', width=150)
        self.tree.column('Payment Method', width=150)
        self.tree.column('Description', width=200)
        self.tree.column('Status', width=100)
        self.tree.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Frame for Subscription Management
        self.subscription_frame = ttk.LabelFrame(self.root, text="Subscription Management", padding="10 10 10 10")
        self.subscription_frame.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        # Labels and entries for Subscriptions
        self.subscription_id_label = ttk.Label(self.subscription_frame, text="Subscription ID:")
        self.subscription_id_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.subscription_id_entry = ttk.Entry(self.subscription_frame)
        self.subscription_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.subscription_member_id_label = ttk.Label(self.subscription_frame, text="Member ID:")
        self.subscription_member_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.subscription_member_id_entry = ttk.Entry(self.subscription_frame)
        self.subscription_member_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.plan_type_label = ttk.Label(self.subscription_frame, text="Plan Type:")
        self.plan_type_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.plan_type_entry = ttk.Entry(self.subscription_frame)
        self.plan_type_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.start_date_label = ttk.Label(self.subscription_frame, text="Start Date (YYYY-MM-DD):")
        self.start_date_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.start_date_entry = ttk.Entry(self.subscription_frame)
        self.start_date_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.end_date_label = ttk.Label(self.subscription_frame, text="End Date (YYYY-MM-DD):")
        self.end_date_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.E)
        self.end_date_entry = ttk.Entry(self.subscription_frame)
        self.end_date_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.subscription_status_label = ttk.Label(self.subscription_frame, text="Status:")
        self.subscription_status_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.E)
        self.subscription_status_entry = ttk.Entry(self.subscription_frame)
        self.subscription_status_entry.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.discount_label = ttk.Label(self.subscription_frame, text="Discount (%):")
        self.discount_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.E)
        self.discount_entry = ttk.Entry(self.subscription_frame)
        self.discount_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons with styles for Subscriptions
        self.add_subscription_button = ttk.Button(self.subscription_frame, text="Add Subscription", command=self.add_subscription)
        self.add_subscription_button.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_subscription_button = ttk.Button(self.subscription_frame, text="Update Subscription", command=self.update_subscription)
        self.update_subscription_button.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

        self.delete_subscription_button = ttk.Button(self.subscription_frame, text="Delete Subscription", command=self.delete_subscription)
        self.delete_subscription_button.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

        self.load_subscription_button = ttk.Button(self.subscription_frame, text="Load Subscriptions", command=self.load_subscriptions)
        self.load_subscription_button.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W)

        # Configure the subscription frame row/column weight for expandability
        for i in range(9):  # Assuming up to 9 rows in the frame
            self.subscription_frame.rowconfigure(i, weight=1)
        for j in range(2):  # Assuming 2 columns
            self.subscription_frame.columnconfigure(j, weight=1)

        # Frame for Treeview for Subscriptions
        self.subscription_tree_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.subscription_tree_frame.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Treeview to display subscriptions
        self.subscription_tree = ttk.Treeview(self.subscription_tree_frame, columns=('ID', 'Member ID', 'Plan Type', 'Start Date', 'End Date', 'Status', 'Discount'), show='headings')
        self.subscription_tree.heading('ID', text='ID')
        self.subscription_tree.heading('Member ID', text='Member ID')
        self.subscription_tree.heading('Plan Type', text='Plan Type')
        self.subscription_tree.heading('Start Date', text='Start Date')
        self.subscription_tree.heading('End Date', text='End Date')
        self.subscription_tree.heading('Status', text='Status')
        self.subscription_tree.heading('Discount', text='Discount')
        self.subscription_tree.column('ID', width=50)
        self.subscription_tree.column('Member ID', width=100)
        self.subscription_tree.column('Plan Type', width=100)
        self.subscription_tree.column('Start Date', width=150)
        self.subscription_tree.column('End Date', width=150)
        self.subscription_tree.column('Status', width=100)
        self.subscription_tree.column('Discount', width=100)
        self.subscription_tree.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure column and row weights to make the layout expandable
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.tree_frame.columnconfigure(0, weight=1)
        self.tree_frame.rowconfigure(0, weight=1)
        self.subscription_tree_frame.columnconfigure(0, weight=1)
        self.subscription_tree_frame.rowconfigure(0, weight=1)

        self.load_payments()
        self.load_subscriptions()

    def add_payment(self):
        try:
            payment = Payment(
                id=int(self.id_entry.get()),
                member_id=int(self.member_id_entry.get()),
                amount=float(self.amount_entry.get()),
                date=datetime.strptime(self.date_entry.get(), '%Y-%m-%d'),
                payment_method=self.payment_method_entry.get(),
                description=self.description_entry.get(),
                status=self.status_entry.get()
            )
            self.payment_manager.add_payment(payment)
            messagebox.showinfo("Success", "Payment added successfully.")
            self.load_payments()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_payment(self):
        try:
            payment = Payment(
                id=int(self.id_entry.get()),
                member_id=int(self.member_id_entry.get()),
                amount=float(self.amount_entry.get()),
                date=datetime.strptime(self.date_entry.get(), '%Y-%m-%d'),
                payment_method=self.payment_method_entry.get(),
                description=self.description_entry.get(),
                status=self.status_entry.get()
            )
            self.payment_manager.update_payment(payment)
            messagebox.showinfo("Success", "Payment updated successfully.")
            self.load_payments()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_payment(self):
        try:
            selected_item = self.tree.selection()[0]
            payment_id = int(self.tree.item(selected_item)['values'][0])
            self.payment_manager.remove_payment(payment_id)
            messagebox.showinfo("Success", "Payment deleted successfully.")
            self.load_payments()
        except IndexError:
            messagebox.showerror("Error", "No payment selected.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_payments(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for payment in self.payment_manager.payments:
            self.tree.insert('', tk.END, values=(payment.id, payment.member_id, payment.amount, payment.date.strftime('%Y-%m-%d'), payment.payment_method, payment.description, payment.status))

    def add_subscription(self):
        try:
            subscription = Subscription(
                id=int(self.subscription_id_entry.get()),
                member_id=int(self.subscription_member_id_entry.get()),
                plan_type=self.plan_type_entry.get(),
                start_date=datetime.strptime(self.start_date_entry.get(), '%Y-%m-%d'),
                end_date=datetime.strptime(self.end_date_entry.get(), '%Y-%m-%d'),
                status=self.subscription_status_entry.get(),
                discount=float(self.discount_entry.get())
            )
            self.payment_manager.add_subscription(subscription)
            messagebox.showinfo("Success", "Subscription added successfully.")
            self.load_subscriptions()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_subscription(self):
        try:
            subscription = Subscription(
                id=int(self.subscription_id_entry.get()),
                member_id=int(self.subscription_member_id_entry.get()),
                plan_type=self.plan_type_entry.get(),
                start_date=datetime.strptime(self.start_date_entry.get(), '%Y-%m-%d'),
                end_date=datetime.strptime(self.end_date_entry.get(), '%Y-%m-%d'),
                status=self.subscription_status_entry.get(),
                discount=float(self.discount_entry.get())
            )
            self.payment_manager.update_subscription(subscription)
            messagebox.showinfo("Success", "Subscription updated successfully.")
            self.load_subscriptions()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_subscription(self):
        try:
            selected_item = self.subscription_tree.selection()[0]
            subscription_id = int(self.subscription_tree.item(selected_item)['values'][0])
            self.payment_manager.remove_subscription(subscription_id)
            messagebox.showinfo("Success", "Subscription deleted successfully.")
            self.load_subscriptions()
        except IndexError:
            messagebox.showerror("Error", "No subscription selected.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def load_subscriptions(self):
        for row in self.subscription_tree.get_children():
            self.subscription_tree.delete(row)
        for subscription in self.payment_manager.subscriptions:
            self.subscription_tree.insert('', tk.END, values=(subscription.id, subscription.member_id, subscription.plan_type, subscription.start_date.strftime('%Y-%m-%d'), subscription.end_date.strftime('%Y-%m-%d'), subscription.status, subscription.discount))
