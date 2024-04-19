def calculate_dose_mg(kg:float):
    return f"{round(2*kg)}ml bolus D10W \r\nthen start {round(80*kg/24)}ml/hr IV D10W \r\n {0.167*round (80*kg/24)*10/kg} mg/kg/min glucose delivery rate"

print(calculate_dose_mg(3.0))