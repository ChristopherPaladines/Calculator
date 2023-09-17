import tkinter as tk

# Function to calculate surplus or deficit
def calculate_budget(income_entry, additional_income_entry, housing_entry, utilities_entry, food_entry, misc_entry, result_label):
    Income = float(income_entry.get())
    additional = float(additional_income_entry.get())
    total_income = Income + additional

    housing = float(housing_entry.get())
    utilities = float(utilities_entry.get())
    food = float(food_entry.get())
    misc = float(misc_entry.get())
    total_expenses = housing + utilities + food + misc

    margin = total_income - total_expenses

    result_label.config(text=f"Your budget next month: ${margin:.2f}")

# Function to clear all input fields
def clear_all(income_entry, additional_income_entry, housing_entry, utilities_entry, food_entry, misc_entry, result_label):
    income_entry.delete(0, tk.END)
    additional_income_entry.delete(0, tk.END)
    housing_entry.delete(0, tk.END)
    utilities_entry.delete(0, tk.END)
    food_entry.delete(0, tk.END)
    misc_entry.delete(0, tk.END)
    result_label.config(text="")

# Create the main application window for the calculator
app = tk.Tk()
app.title("Budget Estimation App")

# Labels and Entry widgets for user input
income_label = tk.Label(app, text="Monthly post-tax income ($USD):")
income_label.grid(row=0, column=0)
income_entry = tk.Entry(app)
income_entry.grid(row=0, column=1)

additional_income_label = tk.Label(app, text="Additional income expected next month ($USD):")
additional_income_label.grid(row=1, column=0)
additional_income_entry = tk.Entry(app)
additional_income_entry.grid(row=1, column=1)

housing_label = tk.Label(app, text="Monthly housing expense ($USD):")
housing_label.grid(row=2, column=0)
housing_entry = tk.Entry(app)
housing_entry.grid(row=2, column=1)

utilities_label = tk.Label(app, text="Monthly utilities expense total ($USD):")
utilities_label.grid(row=3, column=0)
utilities_entry = tk.Entry(app)
utilities_entry.grid(row=3, column=1)

food_label = tk.Label(app, text="Monthly food expense total ($USD):")
food_label.grid(row=4, column=0)
food_entry = tk.Entry(app)
food_entry.grid(row=4, column=1)

misc_label = tk.Label(app, text="Miscellaneous expense total ($USD):")
misc_label.grid(row=5, column=0)
misc_entry = tk.Entry(app)
misc_entry.grid(row=5, column=1)

# Button to calculate budget
calculate_button = tk.Button(app, text="Calculate Budget", command=lambda: calculate_budget(
    income_entry, additional_income_entry, housing_entry, utilities_entry, food_entry, misc_entry, result_label
))
calculate_button.grid(row=6, columnspan=2)

# Button to clear all input fields
clear_button = tk.Button(app, text="Clear All", command=lambda: clear_all(
    income_entry, additional_income_entry, housing_entry, utilities_entry, food_entry, misc_entry, result_label
))
clear_button.grid(row=7, columnspan=2)

# Label to display the result
result_label = tk.Label(app, text="")
result_label.grid(row=8, columnspan=2)

# Start the calculator window
app.mainloop()
