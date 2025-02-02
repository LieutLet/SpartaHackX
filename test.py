import tkinter as tk

from tkinter import Label, Button

popup = tk.Tk()
popup.title("Hypertension and Calculator Info")
popup.geometry("400x400")

def show_hypertension_facts():

    facts = ("HYPERTENSION ANSWER: According to the CDC, Hypertension is persistently high blood pressure at or above 130/80 mm Hg.")

    fact_label = Label(popup, text=facts, wraplength=350, justify="left")

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

    fact_label = Label(popup, text=facts, wraplength=350, justify="left")
    fact_label.pack(pady=10)

hypertension_button = Button(popup, text="What is Hypertension?", command=show_hypertension_facts)
hypertension_button.pack(pady=20)

calculator_button = Button(popup, text="How does the Hypertension Calculator work?", command=show_calculator_facts)
calculator_button.pack(pady=20)

popup.mainloop()