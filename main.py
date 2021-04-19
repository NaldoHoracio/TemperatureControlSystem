import sys, time
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon, QDoubleValidator
from aux_functions import is_valid_temperature, is_range
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QPushButton, QRadioButton, QLineEdit

class TcsMainWindow(QMainWindow):
    def __init__(self):
        super(TcsMainWindow, self).__init__()
        uic.loadUi('TCSystem.ui', self)
        
        # Campos para preenchimento dos valores
        # Modo 1
        self.button_mode1 = self.findChild(QtWidgets.QRadioButton, 'buttonM1')# Botão Mode1

        self.set_temp_m1 = self.findChild(QtWidgets.QLineEdit, 'setTempM1')# Campo setTempM1
        self.set_temp_m1.setToolTip('Input in format: min:s')
        self.set_time_m1 = self.findChild(QtWidgets.QLineEdit, 'setTimeM1')# Campo setTimeM1

        # Modo 2
        self.button_mode2 = self.findChild(QtWidgets.QRadioButton, 'buttonM2')# Botão Mode2
        
        self.set_temp_step_m2 = self.findChild(QtWidgets.QLineEdit, 'tempStepM2')# Campo tempStepM2
        self.set_time_step_m2 = self.findChild(QtWidgets.QLineEdit, 'timeStepM2')# Campo timeStepM2
        self.set_temp_start_m2 = self.findChild(QtWidgets.QLineEdit, 'tempStartM2')# Campo tempStepM2
        self.set_number_steps_m2 = self.findChild(QtWidgets.QLineEdit, 'stepM2')# Campo stepM2

        # Botões para início, pausa ou cancelamento dos processos
        self.button_play = self.findChild(QtWidgets.QPushButton, 'buttonPlay')# Botão Play
        self.button_pause = self.findChild(QtWidgets.QPushButton, 'buttonPause')# Botão Pause
        self.button_cancel = self.findChild(QtWidgets.QPushButton, 'buttonCancel')# Botão Cancel

        self.button_mode1.setChecked(True)# Modo 1 ativo por default
        #self.button_mode2.setChecked(True)# Modo 2 desativado por default

        # Alterando os modos de ativação
        if self.button_mode1.isChecked() == True:
            self.button_mode1.toggled.connect(self.operation_mode)
        else:
            self.button_mode2.toggled.connect(self.operation_mode)
        #self.button_mode2.toggled.connect(self.operation_mode)

        self.update()# Atualiza a janela
        self.show()# Mostra a janela
    
    def play_button_function(self):
        '''
            Função do botão play
        '''
        print("FUNCTION play_button_function INIT")
        print("Botão Play!")
        if self.button_play.isChecked() == True:
            print("Button Play pressed!")
        else:
            print("Button Play unpressed!")
        print("FUNCTION play_button_function END")
    
    def operation_mode_one(self):
        '''
            Função do modo de operaçao 1 (Mode1)
        '''
        print("FUNCTION operation_mode_one INIT")
        print("Operation Mode1")
        #self.play_button_function()
        self.set_temp_m1.setValidator(QDoubleValidator(0.0, 200.0, 1))
        self.set_time_m1.setValidator(QDoubleValidator(0.0, ))
        print("FUNCTION operation_mode_one END")

    def operation_mode_two(self):
        '''
            Função do modo de operaçao 1 (Mode2)
        '''
        print("FUNCTION operation_mode_two INIT")
        print("Operation Mode2")
        self.play_button_function()
        print("FUNCTION operation_mode_two END")
    
    def operation_mode(self) -> None:
        ''' 
            Checa qual modo de operação está ativo
        '''
        print("FUNCTION operation_mode INIT")

        if self.button_mode1.text() == "Mode1":
            if self.button_mode1.isChecked() == True:
                print("Mode 1 activated")
                self.operation_mode_one()
        
        if self.button_mode2.text() == "Mode2":
            if self.button_mode2.isChecked() == True:
                print("Mode 2 activated")
                self.operation_mode_two()
        print("FUNCTION operation_mode END\n")

if __name__ == "__main__":
    
    app_tcs = QtWidgets.QApplication(sys.argv)# Cria uma instância de QApplication
    
    window_obj = TcsMainWindow()# Cria uma instância da classe

    sys.exit(app_tcs.exec_())# Executa a aplicação