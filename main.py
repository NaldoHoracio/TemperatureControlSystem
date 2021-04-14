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

        # Botões para escolha dos modos de operação
        self.button_mode1 = self.findChild(QtWidgets.QRadioButton, 'buttonM1')# Botão Mode1
        self.button_mode2 = self.findChild(QtWidgets.QRadioButton, 'buttonM2')# Botão Mode2
        
        # Campos para preenchimento dos valores
        # Modo 1
        self.set_temp_m1 = self.findChild(QtWidgets.QLineEdit, 'setTempM1')# Campo setTempM1
        self.set_time_m1 = self.findChild(QtWidgets.QLineEdit, 'setTimeM1')# Campo setTimeM1
        # Modo 2
        self.set_temp_step_m2 = self.findChild(QtWidgets.QLineEdit, 'tempStepM2')# Campo tempStepM2
        self.set_time_step_m2 = self.findChild(QtWidgets.QLineEdit, 'timeStepM2')# Campo timeStepM2
        self.set_temp_start_m2 = self.findChild(QtWidgets.QLineEdit, 'tempStartM2')# Campo tempStepM2
        self.set_number_steps_m2 = self.findChild(QtWidgets.QLineEdit, 'stepM2')# Campo stepM2

        # Botões para início, pausa ou cancelamento dos processos
        self.button_play = self.findChild(QtWidgets.QPushButton, 'buttonPlay')# Botão Play
        self.button_pause = self.findChild(QtWidgets.QPushButton, 'buttonPause')# Botão Pause
        self.button_cancel = self.findChild(QtWidgets.QPushButton, 'buttonCancel')# Botão Cancel

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
        print("Mode 1 activated!")
        
        value_temp_m1 = self.set_temp_m1.setValidator(QDoubleValidator(0.1, 220.0, 1))
        
        if self.button_play.setCheckable(True):
            self.button_play.toggled.connect(self.play_button_function)
        else:
            print("Botão Play unpressed!")
        #print("Temp1: ", self.set_temp_m1.text())

        if self.button_pause.setCheckable(True):
            self.button_pause.toggled.connect(self.pause_button_function)
            # print("Para tudo!")
        
        if self.button_cancel.isChecked() == True:
            self.button_cancel.toggled.connect(self.cancel_button_function)
            print("Limpa tudo e gera um .csv com os dados (modo, temperatura, etc).")

    def data_mode_two(self):
        
        #print("Temp2: ", round(set_temp_start_aux,2))
        print("Mode 2 activated!")

    def play_button_function(self):
        # Envia os dados para o arduino e inicia o processo 
        # caso os dados estejam corretos
        print('Play button pressed!')

    def pause_button_function(self):
        # Pausa as tarefa (aquecimento) quando esta
        # em execução
        print("Pause button pressed!")

    def cancel_button_function(self):
        # Cancela a tarefa e limpa todos os campos
        # Retorna ao modo default de abertura: modo 1
        print("Cancel button pressed!")

if __name__ == "__main__":

    app_tcs = QtWidgets.QApplication(sys.argv)# Carrega a aplicação

    window_obj = MainWindow()

    window_obj.show()

    sys.exit(app_tcs.exec())


    
