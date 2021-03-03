import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic, QtWidgets
from aux_functions import is_valid_temperature, is_range

def function_mode_one():
    set_temp_m1 = window_tcs.setTempM1.text()

    if is_valid_temperature(set_temp_m1) == False:
        msg_error = "Invalid temperature!\nEnter a valid format!\nExample: 15.5"
        # QMessageBox.setStyleSheet(self,"background-color: rgb(0,0,0)")
        QMessageBox.critical(window_tcs, "ERRO!", msg_error)
        # set_temp_m1 = window_tcs.setTempM1.text()
    else:
        set_temp_m1 = round(float(set_temp_m1),1)
        if is_range(set_temp_m1) == True:
            print("Sendo to arduin")
            print(set_temp_m1)
        else:
            msg_wrn = "Enter a value in range: 10 °C to 220 °C"
            #QMessageBox.setStyleSheet(self, "background-color: rgb(0,0,0)")
            QMessageBox.critical(window_tcs, "WARNING!", msg_wrn)

def function_mode_two():
    print("Mode 2 select!")

def execution_mode():
    if window_tcs.buttonM1.isChecked() == True:
        function_mode_one()
    else:
        msg_mode1 = "Select mode 1!"
        QMessageBox.critical(window_tcs, "ERRO!", msg_mode1)

    if window_tcs.buttonM2.isChecked() == True:
        function_mode_two()


if __name__ == "__main__":
    app_tcs = QtWidgets.QApplication([])

    window_tcs = uic.loadUi("TCSystem.ui")

    window_tcs.start.clicked.connect(execution_mode)  # Modo de operação

    window_tcs.show()

    app_tcs.exec()  
