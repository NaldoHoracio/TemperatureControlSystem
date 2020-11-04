import sys
from PyQt5 import QtGui
from PyQt5 import uic, QtWidgets

def mode_operation():
    # Verificar se está conectado
    if window_tcs.buttonM1.isChecked():
        print("Mode 1 operation")
        print("Pau na máquina no Mode 1!")
    elif window_tcs.buttonM2.isChecked():
        print("Mode 2 operation")
        print("Pau na máquina no Mode 2!")

app_tcs = QtWidgets.QApplication([])

window_tcs = uic.loadUi("TCSystem.ui")

window_tcs.connButton.clicked.connect(mode_operation)

window_tcs.show()

app_tcs.exec()