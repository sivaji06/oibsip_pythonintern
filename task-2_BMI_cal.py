import tkinter as tk

def calculate_bmi():
    age=int(age_entry.get())
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal Weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    result_label.config(text=f"Your BMI: {bmi:.2f} ({category})")

# Create a tkinter window
window = tk.Tk()
window.title("BMI Calculator")


# Create and place labels and entry fields for weight and height
age_label = tk.Label(window, text=" Enter the Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()


weight_label = tk.Label(window, text="Enter your weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Enter your height (m):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

# Create a button to calculate BMI
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the tkinter main loop
window.mainloop()
