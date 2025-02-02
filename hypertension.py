import numpy as np

class HypertensionCalculator:
    def __init__(self, age, cholesterol, bmi):
        self.age = age
        self.cholesterol = cholesterol
        self.bmi = bmi
    def calculate_hypertension(self):
        try:
            # Logistic regression coefficients (Example values, can be trained)
            beta_0 = -2.5  # Intercept
            beta_1 = 0.02  # Age coefficient
            beta_2 = 0.03  # Cholesterol coefficient
            beta_3 = 0.05  # BMI coefficient

            # Compute linear combination
            Z = beta_0 + (beta_1 * self.age) + (beta_2 * self.cholesterol) + (beta_3 * self.bmi)

            # Compute probability using sigmoid function
            probability = 1 / (1 + np.exp(-Z))

            # Convert probability to percentage
            hypertension_chance = probability * 100

            # Set risk classification
            if hypertension_chance > 50:
                result = f"High Risk ({hypertension_chance:.2f}%)"
            else:
                result = f"Low Risk ({hypertension_chance:.2f}%)"

            return result

        except ValueError:
            return "Please enter valid numerical values."
