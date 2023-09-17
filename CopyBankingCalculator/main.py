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

# Function to start the calculator
def start_calculator():
    # Close the title screen window
    title_screen.destroy()

    # Create the main application window for the calculator
    app = tk.Tk()
    app.title("Budget Estimation App")

    # Labels and Entry widgets for user input (same as before)

    # Buttons (same as before)

    # Label to display the result (same as before)

    # Start the calculator window
    app.mainloop()

# Create the title screen window
title_screen = tk.Tk()
title_screen.title("Budget Calculator Title")

# Title label and start button on the title screen
title_label = tk.Label(title_screen, text="Welcome to the Budget Estimation App")
title_label.pack(pady=20)

start_button = tk.Button(title_screen, text="Start Calculator", command=start_calculator)
start_button.pack()

# Start the title screen window
title_screen.mainloop()
