import sys
from PyQt5 import uic, QtWidgets
from aux_functions import is_valid_temperature


def function_mode_one():
    set_temp_m1 = float(window_tcs.setTempM1.text())
    set_time_m1 = window_tcs.setTimeM1.text()

    if is_valid_temperature(set_temp_m1) == False:
        set_temp_m1 = window_tcs.setTempM1.text()
        print("Enter with a valid format!")
    else:
        print("Send value to arduin!")
        print(round(set_temp_m1, 1))

def function_mode_two():
    print("Mode 2 select!")

def execution_mode():
    # Verificar se está conectado
    if window_tcs.buttonM1.isChecked() == True:
        function_mode_one()
    else:
        print("Show ballon Select mode 1")

    if window_tcs.buttonM2.isChecked() == True:
        function_mode_two()


app_tcs = QtWidgets.QApplication([])

window_tcs = uic.loadUi("TCSystem.ui")

window_tcs.startPause.clicked.connect(execution_mode)  # Modo de operação

window_tcs.show()

app_tcs.exec()
