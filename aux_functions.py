
def is_valid_temperature(temperature):
    try:
        float(temperature)
    except ValueError:
        return False
    return True