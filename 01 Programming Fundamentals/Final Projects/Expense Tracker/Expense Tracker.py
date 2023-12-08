import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        root.title("Expense Tracker")

        self.create_widgets()
        self.setup_layout()

        self.expenses = []
        self.total_expenditure = 0.0

    def create_widgets(self):
        self.amount_label = ttk.Label(self.root, text="Amount:")
        self.amount_entry = ttk.Entry(self.root)

        self.currency_label = ttk.Label(self.root, text="Currency:")
        self.currency_combobox = ttk.Combobox(self.root, values=["USD", "GBP", "EUR"])

        self.category_label = ttk.Label(self.root, text="Category:")
        self.category_combobox = ttk.Combobox(self.root, values=["Life Expenses", "Electricity", "Gas", "Rental", "Grocery", "Savings", "Education", "Charity"])

        self.method_label = ttk.Label(self.root, text="Payment Method:")
        self.method_combobox = ttk.Combobox(self.root, values=["Cash", "Credit Card", "Paypal"])

        self.date_label = ttk.Label(self.root, text="Date:")
        self.date_entry = ttk.Entry(self.root)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        self.add_button = ttk.Button(self.root, text="Add Expense", command=self.add_expense)

        self.tree = ttk.Treeview(self.root, columns=("Amount", "Currency", "Category", "Method", "Date"), show="headings")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Currency", text="Currency")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Method", text="Payment Method")
        self.tree.heading("Date", text="Date")

        self.total_label = ttk.Label(self.root, text="Total Expenditure in USD:")
        self.total_value_label = ttk.Label(self.root, text="0.00")

    def setup_layout(self):
        for i, (label, entry) in enumerate([
            (self.amount_label, self.amount_entry),
            (self.currency_label, self.currency_combobox),
            (self.category_label, self.category_combobox),
            (self.method_label, self.method_combobox),
            (self.date_label, self.date_entry)
        ]):
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
            entry.grid(row=i, column=1, padx=5, pady=5)

        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.tree.grid(row=6, column=0, columnspan=2, pady=10)

        for i, label in enumerate([self.total_label, self.total_value_label]):
            label.grid(row=7, column=i, padx=5, pady=5, sticky="w")

    def add_expense(self):
        amount = self.amount_entry.get()
        currency = self.currency_combobox.get()
        category = self.category_combobox.get()
        method = self.method_combobox.get()
        date_str = self.date_entry.get()

        if not all([amount, currency, category, method, date_str]):
            messagebox.showerror("Error", "All fields must be filled")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount format")
            return

        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
            return

        self.expenses.append((amount, currency, category, method, date))

        self.tree.insert("", "end", values=(amount, currency, category, method, date_str))

        usd_amount = self.convert_to_usd(amount, currency)
        self.total_expenditure += usd_amount

        self.total_value_label.config(text=f"{self.total_expenditure:.2f}")

    def convert_to_usd(self, amount, currency):
        if currency == "USD":
            return amount
        elif currency == "GBP":
            return amount * 1.35
        elif currency == "EUR":
            return amount * 1.18

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
