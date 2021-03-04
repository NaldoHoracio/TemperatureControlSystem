import sys
from PyQt5.QtWidgets import QMessageBox, QPushButton, QApplication
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon
from aux_functions import is_valid_temperature, is_range

def function_mode_one():
    val_mode_1 = True

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
            if return_val_box_error == True:
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
                    val_mode_1 = False
                else:
                    print("Enter a new value in interval 10 to 220")
                    val_mode_1 = True
        

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
