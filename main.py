import sys, time
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton, QRadioButton, QLineEdit
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon, QDoubleValidator
from aux_functions import is_valid_temperature, is_range

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("TCSystem.ui", self)

        self.button_mode1 = self.findChild(QtWidgets.QRadioButton, 'buttonM1')
        self.button_mode2 = self.findChild(QtWidgets.QRadioButton, 'buttonM2')
        #print("Type: ",type(self.buttonM1))
        self.button_mode1.setChecked(True)# Modo 1 ativo por default
        self.button_mode2.setChecked(False)# Modo 2 desativado por default

        # Alterando os modos de ativação
        self.button_mode1.toggled.connect(self.button_state)
        self.button_mode2.toggled.connect(self.button_state)

        #time.sleep(0.1)

        self.show()
            
    
    def button_state(self):
        # Checa qual modo está ativo
        radio_button = self.sender()
        if radio_button.isChecked() == True:
            if radio_button.text() == "Mode1":
                #print("Mode 1 activated!")
                self.data_mode_one()
            elif radio_button.text() == "Mode2":
                #print("Mode 2 activated!")
                self.data_mode_two()
    
    def data_mode_one(self):
        self.set_temp_m1 = self.findChild(QtWidgets.QLineEdit, 'setTempM1')
        self.set_temp_m1.setValidator(QDoubleValidator(0.1, 220.0, 1))
        print("Temp1: ", self.set_temp_m1)
        print("Mode 1 activated!")

    def data_mode_two(self):
        
        #print("Temp2: ", round(set_temp_start_aux,2))
        print("Mode 2 activated!")

if __name__ == "__main__":

    app_tcs = QtWidgets.QApplication(sys.argv)# Load the application

    window_obj = MainWindow()

    window_obj.show()

    sys.exit(app_tcs.exec())


    
