import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class CurrencyConverter:
    # A simple currency converter class with conversion rates
    CONVERSION_RATES = {"USD": 1, "GBP": 1.35, "EUR": 1.18}

    @classmethod
    def convert_to_usd(cls, amount, currency):
        # Convert the given amount to USD based on the specified currency
        rate = cls.CONVERSION_RATES.get(currency, 1)
        return amount * rate

class ExpenseTracker:
    def __init__(self, root):
        # Initialize the main ExpenseTracker application
        self.root = root
        self.root.title("Expense Tracker")

        # Widgets for expense entry
        self.amount_label = ttk.Label(root, text="Amount:")
        self.amount_entry = ttk.Entry(root)

        self.currency_label = ttk.Label(root, text="Currency:")
        self.currency_var = tk.StringVar()
        self.currency_combobox = ttk.Combobox(root, values=["GBP", "EUR", "USD"], textvariable=self.currency_var)

        self.category_label = ttk.Label(root, text="Category:")
        self.category_combobox = ttk.Combobox(root, values=["Life Expenses", "Electricity", "Gas", "Rental", "Grocery", "Savings", "Education", "Charity"])

        self.method_label = ttk.Label(root, text="Payment Method:")
        self.method_combobox = ttk.Combobox(root, values=["Cash", "Credit Card", "Paypal"])

        self.date_label = ttk.Label(root, text="Date:")
        self.date_entry = ttk.Entry(root)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        # Button to add an expense
        self.add_button = ttk.Button(root, text="Add Expense", command=self.add_expense)

        # Treeview to display expenses
        self.tree = ttk.Treeview(root, columns=("Amount", "Currency", "Category", "Method", "Date"), show="headings")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Currency", text="Currency")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Method", text="Payment Method")
        self.tree.heading("Date", text="Date")

        # Labels for total expenditure
        self.total_label = ttk.Label(root, text="Total Expenditure in USD:")
        self.total_value_label = ttk.Label(root, text="0.00")

        # Grid layout for widgets
        self.date_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.currency_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.currency_combobox.grid(row=2, column=1, padx=5, pady=5)

        self.category_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.category_combobox.grid(row=3, column=1, padx=5, pady=5)

        self.method_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.method_combobox.grid(row=4, column=1, padx=5, pady=5)

        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.tree.grid(row=6, column=0, columnspan=2, pady=10)

        self.total_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        self.total_value_label.grid(row=7, column=1, padx=5, pady=5)

        # Initialize expense data and currency converter
        self.expenses = []
        self.currency_converter = CurrencyConverter()

    def validate_fields(self):
        # Check if all entry fields are filled
        fields = [
            self.amount_entry.get(),
            self.currency_var.get(),
            self.category_combobox.get(),
            self.method_combobox.get(),
            self.date_entry.get()
        ]
        return all(fields)

    def add_expense(self):
        # Add an expense to the tracker
        if not self.validate_fields():
            messagebox.showerror("Error", "All fields must be filled")
            return

        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount format")
            return

        try:
            date = datetime.strptime(self.date_entry.get(), "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
            return

        currency = self.currency_var.get()
        self.expenses.append((amount, currency, self.category_combobox.get(), self.method_combobox.get(), date))

        # Insert expense into the Treeview
        self.tree.insert("", "end", values=(amount, currency, self.category_combobox.get(), self.method_combobox.get(), self.date_entry.get()))

        # Update total expenditure label
        usd_amount = self.currency_converter.convert_to_usd(amount, currency)
        self.total_value_label.config(text=f"{sum(self.currency_converter.convert_to_usd(amount, item[1]) for item in self.expenses):.2f}")

if __name__ == "__main__":
    # Create and run the Tkinter application
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
