# importing the required libraries

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# set the title
		self.setWindowTitle("Python")

		# setting geometry
		self.setGeometry(100, 100, 600, 400)

		# creating a push button
		self.button = QPushButton("Toggle", self)

		# setting geometry of button
		self.button.setGeometry(200, 150, 100, 40)

		# setting checkable to true
		self.button.setCheckable(True)

		# setting calling method by button
		self.button.clicked.connect(self.changeColor)

		# setting default color of button to light-grey
		self.button.setStyleSheet("background-color : lightgrey")

		# show all the widgets
		self.update()
		self.show()

	# method called by button
	def changeColor(self):
        if self.button.isChecked() == True:
            self.button.setStyleSheet("background-color : lightblue")
            print("Checked TRUE")
		else:
			self.button.setStyleSheet("background-color : lightgrey")
            print("Checked FALSE")



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

################
################
def default_mode(self):
        print("Modo default activated!")

    def play_button_function(self):
        # Envia os dados para o arduino e inicia o processo 
        # caso os dados estejam corretos
        if self.button_play.isChecked() == True:
            print("PLAY BUTTON M1")
            self.button_play.setStyleSheet("background-color : lightblue")
        else:
            #self.button_play.setCheckab(False)
            self.button_play.setStyleSheet("background-color: lightgrey")
            #self.button_play.setStyleSheet("background-color: rgb(255, 255, 127)")

    def pause_button_function(self):
        # Pausa as tarefa (aquecimento) quando esta
        # em execução
        print("Pause button pressed!")

    def cancel_button_function(self):
        # Cancela a tarefa e limpa todos os campos
        # Retorna ao modo default de abertura: modo 1
        print("Cancel button pressed!")
    
    def operation_mode_one(self):
        '''
            Modo de operação 1 (Mode1)
        '''
        print("FUNCTION operation_mode_one!")   
        #value_temp_m1 = self.set_temp_m1.setValidator(QDoubleValidator(0.1, 220.0, 1))

        if self.button_play.isChecked() == True:
            print("PLAY BUTTON M1")
            self.play_button_function()

        if self.button_pause.setCheckable(True):
            #self.button_pause.toggled()
            #self.pause_button_function()
            print("PAUSE BUTTON M1")
        
        if self.button_cancel.isChecked() == True:
            #self.button_cancel.toggled.connect(self.cancel_button_function)
            #self.button_cancel.toggled()
            #print("Limpa tudo e gera um .csv com os dados (modo, temperatura, etc).")
            print("CANCEL BUTTON M1")
    
    def operation_mode_two(self):
        ''' 
            Modo de operação 2 (Mode2)
        '''     
        print("FUNCTION operation_mode_two!")
        print("Mode 2 activated!")
    
    def operation_mode(self):
        ''' 
            Checa qual modo de operação está ativo
        '''
        if self.button_mode1.isChecked() == True:
            self.operation_mode_one()
            print("Mode 1 button_state")
        
        if self.button_mode2.isChecked() == True:
            self.operation_mode_two()
            print("Mode 2 button_state")
