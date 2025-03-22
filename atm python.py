import tkinter as tk
from tkinter import messagebox, simpledialog

class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Interface")
        self.master.configure(bg="#f0f0f0")  # Light gray background
        self.balance = 1000  # Initial balance
        self.pin = "1217"    # Default PIN
        self.is_authenticated = False

        self.create_widgets()

    def create_widgets(self):
        # Entry for PIN
        self.pin_entry = tk.Entry(self.master, show='*', font=('Arial', 14), bg="#ffffff", fg="#000000")
        self.pin_entry.pack(pady=10)

        # Login button
        self.login_button = tk.Button(self.master, text="Login", command=self.authenticate, bg="#4CAF50", fg="white", font=('Arial', 12))
        self.login_button.pack(pady=5)

        # Buttons for ATM functions, initially disabled
        self.balance_button = tk.Button(self.master, text="Check Balance", command=self.check_balance, state=tk.DISABLED, bg="#2196F3", fg="white", font=('Arial', 12))
        self.balance_button.pack(pady=5)

        self.deposit_button = tk.Button(self.master, text="Deposit Money", command=self.deposit, state=tk.DISABLED, bg="#2196F3", fg="white", font=('Arial', 12))
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(self.master, text="Withdraw Money", command=self.withdraw, state=tk.DISABLED, bg="#2196F3", fg="white", font=('Arial', 12))
        self.withdraw_button.pack(pady=5)

        # Exit button
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit, bg="#f44336", fg="white", font=('Arial', 12))
        self.exit_button.pack(pady=5)

    def authenticate(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.is_authenticated = True
            self.pin_entry.config(state=tk.DISABLED)
            self.login_button.config(state=tk.DISABLED)
            self.balance_button.config(state=tk.NORMAL)
            self.deposit_button.config(state=tk.NORMAL)
            self.withdraw_button.config(state=tk.NORMAL)
            messagebox.showinfo("Login Successful", "You have successfully logged in.")
        else:
            messagebox.showerror("Login Failed", "Incorrect PIN. Please try again.")

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance:.2f}")

    def deposit(self):
        amount = self.get_amount("Enter amount to deposit:")
        if amount is not None:
            self.balance += amount  # Add the deposited amount to the balance
            messagebox.showinfo("Deposit Successful", f"You have successfully deposited ${amount:.2f}.")
            self.check_balance()  # Show updated balance

    def withdraw(self):
        amount = self.get_amount("Enter amount to withdraw:")
        if amount is not None:
            if amount < 100:
                messagebox.showerror("Invalid Amount", "The minimum withdrawal amount is $100.")
            elif amount > self.balance:
                messagebox.showerror("Insufficient Funds", "You do not have enough balance.")
            else:
                self.balance -= amount  # Subtract the withdrawn amount from the balance
                messagebox.showinfo("Withdrawal Successful", f"You have successfully withdrawn ${amount:.2f}.")
                self.check_balance()  # Show updated balance

    def get_amount(self, prompt):
        amount_str = simpledialog.askstring("Input", prompt)
        if amount_str is not None:
            try:
                amount = float(amount_str)
                if amount > 0:
                    return amount
                else:
                    messagebox.showerror("Invalid Amount", "Please enter a positive amount.")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return None

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()