import tkinter as tk
class BMIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced BMI Calculator")

        # Create input fields
        self.weight_label = tk.Label(self, text="Weight (kg):")
        self.weight_label.grid(row=0, column=0)
        self.weight_entry = tk.Entry(self)
        self.weight_entry.grid(row=0, column=1)

        self.height_label = tk.Label(self, text="Height (cm):")
        self.height_label.grid(row=1, column=0)
        self.height_entry = tk.Entry(self)
        self.height_entry.grid(row=1, column=1)

        # Calculate button
        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, columnspan=2)

        # Result display
        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=3, columnspan=2)

    def calculate_bmi(self):
        weight = float(self.weight_entry.get())
        height = float(self.height_entry.get()) / 100
        bmi = weight / (height ** 2)
        self.display_result(bmi)

    def display_result(self, bmi):
        category = self.get_category(bmi)
        self.result_label.config(text=f"BMI: {bmi:.2f}, Category: {category}")

    def get_category(self, bmi):
        # Categorize BMI
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
#runs the main gui
if __name__ == "__main__":
    app = BMIApp()
    app.mainloop()






