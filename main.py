import sys
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtWidgets import QPushButton, QRadioButton
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from aux_functions import is_valid_temperature, is_range

def read_data_mode_one():
    # Function Mode 1 operation
    # Actives fields: Set temperature, Set time
    # Read the temperature until you enter a correct value
    print("Mode 1 select!\n")
    """ val_mode_1 = True

    while (val_mode_1 == True):
        set_temp_m1 = window_tcs.setTempM1.text()

        if is_valid_temperature(set_temp_m1) == False:
            msg_error = "Invalid temperature!\nEnter a valid format!\nExample: 15.5"
            box_error = QMessageBox()
            box_error.setIcon(QMessageBox.Critical)
            box_error.setText(msg_error)
            box_error.setWindowTitle("Value of the temperature")
            # QMessageBox.setStyleSheet(self,"background-color: rgb(0,0,0)")
            box_error.setStandardButtons(QMessageBox.Ok)

            return_val_box_error = box_error.exec()
            if return_val_box_error == QMessageBox.Ok:
                print(msg_error)
                val_mode_1 = True
        else:
            set_temp_m1 = round(float(set_temp_m1),1)
            if is_range(set_temp_m1) == True:
                print("Sendo to arduin")
                print(set_temp_m1)
                val_mode_1 = False
            else:
                msg_wrn = "Enter a value in range: 10 °C to 220 °C"
                box_warning = QMessageBox()
                box_warning.setIcon(QMessageBox.Warning)
                box_warning.setText(msg_wrn)
                box_warning.setWindowTitle("Range of the temperature")
                box_warning.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                
                return_val_box_warning = box_warning.exec()
                if return_val_box_warning == QMessageBox.Ok:
                    print("Ok! Continue")
                    val_mode_1 = True """

def read_data_mode_two():
    # Function Mode 2 operation
    # Actives fields: Step size: time, Temperature start, Step size: temperature, 
    # Number of steps, Current steps
    # Read the temperature until you enter a correct value 
    print("Mode 2 select!\n")

def button_state():
    button = QRadioButton()
    # Mode 1 select
    if button.text() == "Mode1":
        # Deactivate Mode 2
        if button.isChecked() == True:
            print("Input button state function\n")
            print("Mode 1 active!")
            #read_data_mode_one()
        else:
            print("Mode 1 deactivate!\n")
    # Mode 2 select
    if button.text() == "Mode2":
        # Deactivate Mode 1
        if button.isChecked() == True:
            print("Input button state function\n")
            print("Mode 2 active!")
            #read_data_mode_two()
        else:
            print("Mode 2 deactivate!\n")

'''
def select_mode():
    # Buttons m1 e m2
    button_mode1 = window_tcs.buttonM1()
    button_mode2 = window_tcs.buttonM2()

    button_mode1.setChecked(True)# Active for default
    button_mode2.setChecked(False)# Deactive for default

    button_mode1.toggled.connect(button_state())

    button_mode2.toggled.connect(button_state())
'''

if __name__ == "__main__":
    app_tcs = QtWidgets.QApplication([])

    window_tcs = uic.loadUi("TCSystem.ui")

    window_tcs.buttonM1.toggled.connect(button_state)# Execution mode 1
    window_tcs.buttonM2.toggled.connect(button_state)# Execution mode 2
    # window_tcs.buttonPlay.connect()
    window_tcs.show()

    app_tcs.exec()  
