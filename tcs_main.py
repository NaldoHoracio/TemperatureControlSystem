import sys
from PyQt5 import uic, QtWidgets, QMessageBox
from aux_functions import is_valid_numer

def function_mode_one():
    set_temp_mode_one = window_tcs.setTempM1.text()
    if window_tcs.buttonM1.isChecked() == False:
        print("Exibir que o modo 1 não foi selecionado!")
    else:
        print(set_temp_mode_one)
    set_time_mode_one = windows_tcs.setTimeM1.text()

def execution_mode():
    # Verificar se está conectado
    if window_tcs.buttonM1.isChecked() == True:
        function_mode_one()
    elif window_tcs.buttonM2.isChecked() == True:
        print("Mode 2 operation")
        print("Pau na máquina no Mode 2!")

app_tcs = QtWidgets.QApplication([])

window_tcs = uic.loadUi("TCSystem.ui")

window_tcs.startPause.clicked.connect(execution_mode) # Modo de operação

window_tcs.show()

app_tcs.exec()