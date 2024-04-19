import Amp


def calculate_dose_mg(kg:float):
    return f"{round(4*kg)}mg IV Gentamicin q24hr"
print(calculate_dose_mg(2.3))