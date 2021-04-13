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
        value_temp_m1 = self.set_temp_m1.setValidator(QDoubleValidator(0.1, 220.0, 1))
        
        # Botão Play
        self.button_play = self.findChild(QtWidgets.QPushButton, 'buttonPlay')

        if self.button_play.clicked.connect(self.button_play):
            if value_temp_m1 == True:
                print("Mode 1 activated! Segue o baile!")
            else:
                msg_err_temp_m1 = QMessageBox()
                msg_err_temp_m1.setIcon(QMessageBox.Information)
                msg_err_temp_m1.setText("Invalid format or \
                    temperature outside the range or incomplete data! \
                    Check the problem and input the values.")
                msg_err_temp_m1.setWindowTitle("Warning")
                msg_err_temp_m1.setStandardButtons(QMessageBox.Ok)
                
                return_val_set_temp_m1 = msg_err_temp_m1.exec()
                
                if return_val_set_temp_m1 == QMessageBox.Ok:
                    pass
                


        #print("Temp1: ", self.set_temp_m1.text())
        print("Mode 1 activated!")

    def data_mode_two(self):
        
        #print("Temp2: ", round(set_temp_start_aux,2))
        print("Mode 2 activated!")

    def button_play(self):
        # Envia os dados para o arduino e inicia o processo 
        # caso os dados estejam corretos
        print('Play button click')

if __name__ == "__main__":

    app_tcs = QtWidgets.QApplication(sys.argv)# Carrega a aplicação

    window_obj = MainWindow()

    window_obj.show()

    sys.exit(app_tcs.exec())


    
