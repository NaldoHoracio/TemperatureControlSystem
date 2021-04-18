import sys, time
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton, QRadioButton, QLineEdit
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon, QDoubleValidator
from aux_functions import is_valid_temperature, is_range

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("TCSystem.ui", self)
        
        # Campos para preenchimento dos valores
        # Modo 1
        self.button_mode1 = self.findChild(QtWidgets.QRadioButton, 'buttonM1')# Botão Mode1
        self.set_temp_m1 = self.findChild(QtWidgets.QLineEdit, 'setTempM1')# Campo setTempM1
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
        self.button_mode2.setChecked(False)# Modo 2 desativado por default

        # Captura o modo default de ativação quando abre a janela
        #if self.button_mode1.isChecked() == True:
        #    #print("Mode 1 IF")
        #    self.button_mode1.toggled.connect(self.operation_mode)

        # Alterando os modos de ativação
        self.button_mode1.toggled.connect(lambda:self.operation_mode)
        self.button_mode2.toggled.connect(lambda:self.operation_mode)

        #self.update()
        #self.show()
    
    def operation_mode(self):
        ''' 
            Checa qual modo de operação está ativo
        '''
        if self.button_mode1.isChecked() == True:
            #self.operation_mode_one()
            print("Mode 1 button_state")
        
        if self.button_mode2.isChecked() == True:
            #self.operation_mode_two()
            print("Mode 2 button_state")

if __name__ == "__main__":

    app_tcs = QtWidgets.QApplication(sys.argv)# Carrega a aplicação

    window_obj = MainWindow()

    window_obj.show()

    sys.exit(app_tcs.exec())