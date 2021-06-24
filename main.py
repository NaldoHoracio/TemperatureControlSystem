import sys, time
import aux_functions
from tkinter import * 
from tkinter import messagebox
from PyQt5.QtCore import QTime
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QIcon, QDoubleValidator
#from aux_functions import is_valid_temperature, is_range
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, \
QPushButton, QRadioButton, QLineEdit, QTimeEdit

class TcsMainWindow(QMainWindow):
    def __init__(self):
        super(TcsMainWindow, self).__init__()
        uic.loadUi('TCSystem.ui', self)
        
        # Campos para preenchimento dos valores
        # MODO 1
        self.button_mode1 = self.findChild(QtWidgets.QRadioButton, 'buttonM1')# Botão Mode1

        self.set_temp_m1 = self.findChild(QtWidgets.QDoubleSpinBox, 'setTempM1')# Campo setTempM1
        self.set_temp_m1.setToolTip('Example input: 15.2')# Help para mostrar o tipo de dado na entrada

        self.set_time_m1 = self.findChild(QtWidgets.QTimeEdit, 'setTimeM1')# Campo setTimeM1
        self.set_time_m1.setTimeRange(QTime(0, 00, 00), QTime(0, 59, 59))# Limitando a entrada
        self.set_time_m1.setDisplayFormat('mm:ss')
        self.set_time_m1.setToolTip('Example input: 02:30')

        # MODO 2
        self.button_mode2 = self.findChild(QtWidgets.QRadioButton, 'buttonM2')# Botão Mode2
        
        self.set_time_step_m2 = self.findChild(QtWidgets.QTimeEdit, 'timeStepM2')# Campo timeStepM2
        self.set_time_step_m2.setTimeRange(QTime(0, 00, 00), QTime(0, 59, 59))# Limitando a entrada
        self.set_time_step_m2.setDisplayFormat('mm:ss')# Limitando a entrada no objeto
        self.set_time_step_m2.setToolTip('Example input: 02:30')# Help para mostrar o tipo de dado na entrada

        self.set_temp_start_m2 = self.findChild(QtWidgets.QDoubleSpinBox, 'tempStartM2')# Campo tempStepM2
        self.set_temp_start_m2.setToolTip('Example input: 15.2')# Help para mostrar o tipo de dado na entrada

        self.set_number_steps_m2 = self.findChild(QtWidgets.QSpinBox, 'stepM2')# Campo stepM2
        self.set_number_steps_m2.setToolTip('Example input: 5')

        # Botões para início, pausa ou cancelamento dos processos
        self.button_play = self.findChild(QtWidgets.QPushButton, 'buttonPlay')# Botão Play
        self.button_play.setCheckable(True)

        self.button_pause = self.findChild(QtWidgets.QPushButton, 'buttonPause')# Botão Pause
        self.button_pause.setCheckable(True)

        self.button_cancel = self.findChild(QtWidgets.QPushButton, 'buttonCancel')# Botão Cancel
        self.button_cancel.setCheckable(True)

        self.button_mode1.setChecked(True)# Modo 1 ativo por default
        #self.button_mode2.setChecked(True)# Modo 2 desativado por default

        # Alterando os modos de ativação
        if self.button_mode1.isChecked() == True:
            self.button_play.clicked.connect(self.play_button_function)
            self.button_pause.clicked.connect(self.pause_button_function)
            self.button_cancel.clicked.connect(self.cancel_button_function)
        else:
            self.button_play.clicked.connect(self.play_button_function)
            self.button_pause.clicked.connect(self.pause_button_function)
            self.button_cancel.clicked.connect(self.cancel_button_functions)
        #self.button_mode2.toggled.connect(self.operation_mode)

        self.update()# Atualiza a janela
        self.show()# Mostra a janela
    
    def play_button_function(self):
        '''
            Função do botão Play
        '''
        if self.button_mode1.isChecked() == True:
            if self.button_play.isChecked() == True:
                messagebox.showinfo("Info", "Button Play pressed MODE 1")
            else:
                messagebox.showinfo("Info", "Button Play unpressed MODE 1")
        else:
            if self.button_play.isChecked() == True:
                messagebox.showinfo("Info", "Button Play pressed MODE 2")
            else:
                messagebox.showinfo("Info", "Button Play unpressed MODE 2")

    
    def pause_button_function(self):
        '''
            Função do botão Pause
        '''
        if self.button_mode1.isChecked() == True:
            if self.button_pause.isChecked() == True:
                messagebox.showinfo("Info", "Button Pause pressed MODE 1")
            else:
                messagebox.showinfo("Info", "Button Pause unpressed MODE 1")
        else:
            if self.button_pause.isChecked() == True:
                messagebox.showinfo("Info", "Button Pause pressed MODE 2")
            else:
                messagebox.showinfo("Info", "Button Pause unpressed MODE 2")
    
    def cancel_button_function(self):
        '''
            Função do botão Cancel
        '''
        if self.button_mode1.isChecked() == True:
            if self.button_cancel.isChecked() == True:
                messagebox.showinfo("Info", "Pressed Cancel MODE 1")
            else:
                messagebox.showinfo("Info", "Pressed Cancel MODE 1")
        else:
            if self.button_cancel.isChecked() == True:
                messagebox.showinfo("Info", "Pressed Cancel MODE 2")
            else:
                messagebox.showinfo("Info", "Pressed Cancel MODE 2")
                
                  
  
if __name__ == "__main__":
    
    app_tcs = QApplication(sys.argv)# Cria uma instância de QApplication
    
    window_obj = TcsMainWindow()# Cria uma instância da classe

    sys.exit(app_tcs.exec())# Executa a aplicação