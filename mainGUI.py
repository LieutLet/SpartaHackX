import tkinter as tk
from hypertension import HypertensionCalculator

# Function to add a new entry box
#def add_entry():
#    new_entry = tk.Entry(table_frame, font=("Arial", 14))
#    new_entry.pack(fill=tk.X, pady=5, padx=10)
#    entry_boxes.append(new_entry)

age = "0"
cholesterol ="0"
bmi ="0"
RiskofHyTn = "No Input"
stats = stats = HypertensionCalculator(float(age), float(cholesterol), float(bmi))

#Gets the Entry value from all the entry boxes so they can be sent into the calculation
def get_Value():
    age = float(ageEntry.get())
    cholesterol = float(cholestralEntry.get())
    bmi = float(BMIEntry.get())
    RiskofHyTn = stats.calculate_hypertension()
    results = tk.Label(root, text = RiskofHyTn, font = ("Arial", 18))
    results.pack(pady = 20)
    #print("Age: ", age, " Cholestrol: ", cholesterol, " BMI: ", bmi, "Result: ", RiskofHyTn )
    


#def get_Value_Cho():

#def get_Value_BMI():

# Create the main window
root = tk.Tk()
root.title("Risk of Hypertension Calculator")

# Create a frame for the menu icon
menu_frame = tk.Frame(root, bg="grey", height=50)
menu_frame.pack(fill=tk.X)

# Create a hamburger menu icon
hamburger_icon = tk.Label(menu_frame, text="☰", font=("Arial", 18), bg="grey", fg="white")
hamburger_icon.pack(side=tk.LEFT, padx=10, pady=5)

# Create a label for the title
title_label = tk.Label(root, text="Risk of Hypertension Calculator", font=("Arial", 16))
title_label.pack(pady=10)

# Create the Calculate button
calculate_button = tk.Button(root, text="Calculate", command = get_Value, font=("Arial", 14), bg="black", fg="white")
calculate_button.pack(pady=10)

# Create a frame for the table
table_frame = tk.Frame(root)
table_frame.pack(pady=10)

# Create initial entry boxes
entry_boxes = []

# BMI Entry
bmi_frame = tk.Frame(table_frame)
bmi_frame.pack(fill=tk.X, pady=5)
bmi_label = tk.Label(bmi_frame, text="BMI:", font=("Arial", 14), width=15, anchor="w")
bmi_label.pack(side=tk.LEFT, padx=10)
BMIEntry = tk.Entry(bmi_frame, font=("Arial", 14))
BMIEntry.pack(fill=tk.X, padx=10)
entry_boxes.append(BMIEntry)

# Cholesterol Entry
cholesterol_frame = tk.Frame(table_frame)
cholesterol_frame.pack(fill=tk.X, pady=5)
cholesterol_label = tk.Label(cholesterol_frame, text="Cholesterol:", font=("Arial", 14), width=15, anchor="w")
cholesterol_label.pack(side=tk.LEFT, padx=10)
cholestralEntry = tk.Entry(cholesterol_frame, font=("Arial", 14))
cholestralEntry.pack(fill=tk.X, padx=10)
entry_boxes.append(cholestralEntry)

# Age Entry
age_frame = tk.Frame(table_frame)
age_frame.pack(fill=tk.X, pady=5)
age_label = tk.Label(age_frame, text="Age:", font=("Arial", 14), width=15, anchor="w")
age_label.pack(side=tk.LEFT, padx=10)
ageEntry = tk.Entry(age_frame, font=("Arial", 14))
ageEntry.pack(fill=tk.X, padx=10)
entry_boxes.append(ageEntry)

#Results


# Create a plus sign button to add more entry boxes
#plus_button = tk.Button(root, text="+", font=("Arial", 20), command=add_entry)
#plus_button.pack(pady=10)

# Run the application
root.mainloop()