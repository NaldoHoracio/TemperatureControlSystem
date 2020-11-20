from PyQt5.QtWidgets import QMessageBox

def is_valid_temperature(temperature):
    ''' 
    # This function validating the input temperature
    
    # keyword arguments:
    temperature: string

    # return: True or False
    '''
    try:
        float(temperature)
    except ValueError:
        return False
    return True

def is_range(temperature):
    ''' 
    # This function checks if the temperature is in the range
    
    # keyword arguments:
    temperature: temperature

    # return: True or False
    '''
    if temperature >= 10.0 and temperature <= 220.0:
        return True
    else:
        return False
