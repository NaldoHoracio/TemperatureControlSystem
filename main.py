import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import uic, QtWidgets
from aux_functions import is_valid_temperature, is_range

def teste_print():
    print("Hello world!")

def function_mode_one():
    set_temp_m1 = float(window_tcs.setTempM1.text())
    set_time_m1 = window_tcs.setTimeM1.text()

    if is_valid_temperature(set_temp_m1) == False:
        msg_error = "Enter a valid format!\nExample: 15.5"
        # QMessageBox.setStyleSheet(self,"background-color: rgb(0,0,0)")
        QMessageBox.critical(window_tcs, "ERRO!", msg_error)
        # set_temp_m1 = window_tcs.setTempM1.text()
    else:
        if is_range(set_temp_m1) == True:
            print("Sendo to arduin")
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
