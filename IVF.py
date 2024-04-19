def calculate_dose_mg(kg:float):
    return f"{round(20*kg)}ml IV bolus over 1hr \r\n {4*kg} ml/hr mIVF \r\n {round(0.5*kg/24,4)} hourly UOP goal"
print(calculate_dose_mg(2.3))