import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class Window_Tcs (QMainWindow):
    def __init__(self):
        super(Window_Tcs, self).__init__()

        # Parâmetros da Janela
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "TCSystem"

        # Caixas de texto
        self.insertTimes = QLineEdit(self)
        self.insertTimes.move(700,340)
        self.insertTimes.resize(100,50)

        self.tempStart = QLineEdit(self)
        self.tempStart.move(700, 410)
        self.tempStart.resize(100, 50)

        self.tempStep = QLineEdit(self)
        self.tempStep.move(700, 480)
        self.tempStep.resize(100, 50)

        self.numbStep = QLineEdit(self)
        self.numbStep.move(700, 550)
        self.numbStep.resize(100, 50)

        self.numbStep = QLineEdit(self)
        self.numbStep.move(700, 620)
        self.numbStep.resize(100, 50)

        # BOTÕES
        buttonConnect = QPushButton('Connect', self)
        buttonConnect.move(30,30) # .move(width_position, height_position)
        buttonConnect.resize(100,50) # .resize(width_button, height_button)
        buttonConnect.setStyleSheet('QPushButton {background-color:#800000;font:bold}')
        buttonConnect.clicked.connect(self.buttonConnectClick)

        buttonMode1 = QPushButton('Mode 1', self)
        buttonMode1.move(230, 30)  # .move(width_position, height_position)
        buttonMode1.resize(100, 50)  # .resize(width_button, height_button)
        buttonMode1.setStyleSheet('QPushButton')
        buttonMode1.clicked.connect(self.buttonMode1Click)

        buttonMode2 = QPushButton('Mode 2', self)
        buttonMode2.move(350, 30)  # .move(width_position, height_position)
        buttonMode2.resize(100, 50)  # .resize(width_button, height_button)
        buttonMode2.setStyleSheet('QPushButton')
        buttonMode2.clicked.connect(self.buttonMode2Click)

        buttonStartPause = QPushButton('Start/Pause', self)
        buttonStartPause.move(700, 200)  # .move(width_position, height_position)
        buttonStartPause.resize(100, 50)  # .resize(width_button, height_button)
        buttonStartPause.setStyleSheet('QPushButton')
        buttonStartPause.clicked.connect(self.buttonStartPauseClick)

        buttonCancel = QPushButton('Cancel', self)
        buttonCancel.move(700, 270)  # .move(width_position, height_position)
        buttonCancel.resize(100, 50)  # .resize(width_button, height_button)
        buttonCancel.setStyleSheet('QPushButton')
        buttonCancel.clicked.connect(self.buttonCancelClick)

        self.LoadWindow()

    # Método para carregar janela
    def LoadWindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    # Método para o botão de conexão
    def buttonConnectClick(self):
        print("Load Port of Arduino UNO!")

    # Método para o botão Mode1
    def buttonMode1Click(self):
        print("Mode 1!")

    # Método para o botão Mode1
    def buttonMode2Click(self):
        print("Mode 2!")

    # Método para o botão Mode1
    def buttonStartPauseClick(self):
        print("Start/Pause!")

    def buttonCancelClick(self):
        print("Cancel")

application = QApplication(sys.argv)
j_tcs = Window_Tcs()
sys.exit(application.exec())