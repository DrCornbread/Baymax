def calculate_dose_mg(kg:float):
    """Calculates Ampicillin dose for infants

    Args:
        kg (float): Baby's weight in Kg's
    Returns:
       str: Dose note statement containing dose in mg
    """
    return f"{round(100*kg)}mg IV Ampicillin TID"


print(calculate_dose_mg(2.3))