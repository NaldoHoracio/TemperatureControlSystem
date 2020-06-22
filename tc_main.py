import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Window_Tcs (QMainWindow):
    def __init__(self):
        super(Window_Tcs, self).__init__()

        # Parâmetros da Janela
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "TCSystem"

        # Botões
        buttonConnect = QPushButton('Button Connect', self)
        buttonConnect.move(30,30) # .move(width_position, height_position)
        buttonConnect.resize(100,50) # .resize(width_button, height_button)
        buttonConnect.setStyleSheet('QPushButton {background-color:#800000;font:bold}')
        buttonConnect.clicked.connect(self.buttonConnectClick)


        self.LoadWindow()

    # Método para carregar janela
    def LoadWindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    # Método para o botão de conexão
    def buttonConnectClick(self):
        print("Load Port of Arduino UNO!")

application = QApplication(sys.argv)
j_tcs = Window_Tcs()
sys.exit(application.exec())