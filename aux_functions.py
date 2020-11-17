
def is_valid_numer(temperature):
    try:
        float(temperature)
    except ValueError:
        return False
    return True