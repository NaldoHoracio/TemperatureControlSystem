import sys, time
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton, QRadioButton, QLineEdit
from PyQt5 import uic, QtWidgets, QHBoxLayout
from PyQt5.QtGui import QIcon, QDoubleValidator
from aux_functions import is_valid_temperature, is_range
		
class Radiodemo(QWidget):

   def __init__(self, parent = None):
      super(Radiodemo, self).__init__(parent)
		
      layout = QHBoxLayout()
      self.b1 = QRadioButton("Button1")
      self.b1.setChecked(True)
      self.b1.toggled.connect(lambda:self.btnstate(self.b1))
      layout.addWidget(self.b1)
		
      self.b2 = QRadioButton("Button2")
      self.b2.toggled.connect(lambda:self.btnstate(self.b2))

      layout.addWidget(self.b2)
      self.setLayout(layout)
      self.setWindowTitle("RadioButton demo")
		
   def btnstate(self,b):
	
      if b.text() == "Button1":
         if b.isChecked() == True:
            print(b.text()+" is selected")
         else:
            print(b.text()+" is deselected")
				
      if b.text() == "Button2":
         if b.isChecked() == True:
            print(b.text()+" is selected")
         else:
            print(b.text()+" is deselected")
				
def main():

   app = QApplication(sys.argv)
   ex = Radiodemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()


def operation_mode(self):
        # Checa qual modo está ativo
        if self.button_mode1.isChecked() == True:
            self.operation_mode_one()
            print("Mode 1 button_state")
        
        if self.button_mode2.isChecked() == True:
            self.operation_mode_two()
            print("Mode 2 button_state")

super().__init__()

        uic.loadUi("TCSystem.ui", self)# Call the window

        self.buttonM1.setChecked(True)# Active for default
        self.buttonM2.setChecked(False)# Deactive for default

        self.buttonM1.toggled.connect(button_state())

        self.buttonM2.toggled.connect(button_state())

    def button_state(self):
        radio_button = self.sender()
        # Mode 1 select
        if radio_button.text() == "Mode1":
        # Deactivate Mode 2
            if radio_button.isChecked() == True:
                print("Input button state function\n")
                print("Mode 1 active!")
                #read_data_mode_one()
            else:
                print("Mode 1 deactivate!\n")
        # Mode 2 select
        if radio_button.text() == "Mode2":
            # Deactivate Mode 1
            if radio_button.isChecked() == True:
                print("Input button state function\n")
                print("Mode 2 active!")
                read_data_mode_two()
            else:
                print("Mode 2 deactivate!\n")

    def read_data_mode_one():
        # Function Mode 1 operation
        # Actives fields: Set temperature, Set time
        # Read the temperature until you enter a correct value
            print("Mode 1 select!\n")
            """ val_mode_1 = True

            while (val_mode_1 == True):
                set_temp_m1 = window_tcs.setTempM1.text()

                if is_valid_temperature(set_temp_m1) == False:
                    msg_error = "Invalid temperature!\nEnter a valid format!\nExample: 15.5"
                    box_error = QMessageBox()
                    box_error.setIcon(QMessageBox.Critical)
                    box_error.setText(msg_error)
                    box_error.setWindowTitle("Value of the temperature")
                    # QMessageBox.setStyleSheet(self,"background-color: rgb(0,0,0)")
                    box_error.setStandardButtons(QMessageBox.Ok)

                    return_val_box_error = box_error.exec()
                    if return_val_box_error == QMessageBox.Ok:
                        print(msg_error)
                        val_mode_1 = True
                else:
                    set_temp_m1 = round(float(set_temp_m1),1)
                    if is_range(set_temp_m1) == True:
                        print("Sendo to arduin")
                        print(set_temp_m1)
                        val_mode_1 = False
                    else:
                        msg_wrn = "Enter a value in range: 10 °C to 220 °C"
                        box_warning = QMessageBox()
                        box_warning.setIcon(QMessageBox.Warning)
                        box_warning.setText(msg_wrn)
                        box_warning.setWindowTitle("Range of the temperature")
                        box_warning.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                        
                        return_val_box_warning = box_warning.exec()
                        if return_val_box_warning == QMessageBox.Ok:
                            print("Ok! Continue")
                            val_mode_1 = True """

    def read_data_mode_two():
        # Function Mode 2 operation
        # Actives fields: Step size: time, Temperature start, Step size: temperature, 
        # Number of steps, Current steps
        # Read the temperature until you enter a correct value 
        print("Mode 2 select!\n")




if __name__ == "__main__":

    app_tcs = QtWidgets.QApplication([])# Load the application

    window_obj = MainWindow()

    window_obj.show()

    sys.exit(app_tcs.exec())
    #window_tcs = uic.loadUi("TCSystem.ui")# Call the window

    # while janela_principal executando chame a função de seleção dos botões
    #while True:
        # Mode select - Mode1 or Mode2
    #window_tcs.buttonM1.setChecked(True)# Active for default
    #window_tcs.buttonM2.setChecked(False)# Deactive for default

    #window_tcs.buttonM1.toggled.connect(button_state())

    #window_tcs.buttonM2.toggled.connect(button_state())
        #time.sleep(0.1)
    
    # window_tcs.buttonPlay.connect()

    ### Pressed button actions

    '''
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
               ''' 