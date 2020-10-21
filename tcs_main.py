from PyQt5 import uic, QtWidgets

def mode1():
    if window_tcs.buttonM1.isChecked():
        print("Mode 1 select!")

def connectButton():
    print("Abrir devices USBs")

app_tcs = QtWidgets.QApplication([])

window_tcs = uic.loadUi("TCSystem.ui")

window_tcs.connButton.clicked.connect(connectButton)

window_tcs.show()

app_tcs.exec()