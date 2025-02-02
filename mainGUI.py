import tkinter as tk
from hypertension import HypertensionCalculator

def get_Value():
    try:
        age = float(ageEntry.get())
        cholesterol = float(cholestralEntry.get())
        bmi = float(BMIEntry.get())
        
        # Debug prints to check input values
        print(f"Input Age: {age}, Input Cholesterol: {cholesterol}, Input BMI: {bmi}")
        
        stats = HypertensionCalculator(age, cholesterol, bmi)
        RiskofHyTn = stats.calculate_hypertension()
        
        # Debug print to check the result
        print(f"Result: {RiskofHyTn}")
        
        results = tk.Label(root, text=RiskofHyTn, font=("Arial", 18))
        results.pack(pady=20)
    except Exception as e:
        print(f"Error: {e}")

root = tk.Tk()
root.title("Risk of Hypertension Calculator")

# Create a frame for the menu icon
menu_frame = tk.Frame(root, bg="grey", height=50)
menu_frame.pack(fill=tk.X)

def show_hypertension_facts():

    facts = ("HYPERTENSION ANSWER: According to the CDC, Hypertension is persistently high blood pressure at or above 130/80 mm Hg.")
    fact_label = tk.Label(root, text=facts, wraplength=350, justify="left")
    fact_label.pack(pady=10)

def show_calculator_facts():
    facts = (
        "CALCULATOR ANSWER: Logistic regression was the statistical method used for predicting one's Hypertension risk "
        "The three independent variables used to predict one's risk were age, BMI, and cholesterol level. "
        "The outcome is measured with a variable representing two possible outcomes. "
        "The logistic regression formula is:\n\n"
        "P(Y=1) = 1 / (1 + e^-(-2.5 + 0.02*age + 0.03*cholesterol + 0.05*BMI))\n\n"
        "where P(Y=1) is the predicted Hypertension risk, and e is the base of the natural logarithm. "
    )
    fact_label = tk.Label(root, text=facts, wraplength=350, justify="left")
    fact_label.pack(pady=10)

hypertension_button = tk.Button(root, text="What is Hypertension?", command=show_hypertension_facts)
hypertension_button.pack(pady=20)

calculator_button = tk.Button(root, text="How does the Hypertension Calculator work?", command=show_calculator_facts)
calculator_button.pack(pady=20) 

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

root.mainloop()