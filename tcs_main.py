from PyQt5 import uic, QtWidgets

def connect_button():
        print("Abrir devices USBs")

if windows_tcs.buttonM1.isChecked():
    print("Teste M1")
    def mode1_function():
        # Verificar se está conectado
        set_temperature = windows_tcs.setTempM1.text()
        print("Set temperature: ", type(set_tempterature))
elif windows_tcs.buttonM2.isChecked():
    # Verificar se está conectado
    print("Teste M2")

app_tcs = QtWidgets.QApplication([])

window_tcs = uic.loadUi("TCSystem.ui")

window_tcs.connButton.clicked.connect(connectButton)

window_tcs.show()

app_tcs.exec()