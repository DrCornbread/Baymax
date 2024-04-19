def calculate_dose_mg(kg:float):
    return f"{round(100*kg)}mg IV Ampicillin TID"


print(calculate_dose_mg(2.3))