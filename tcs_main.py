from PyQt5 import uic, QtWidgets

application = QtWidgets.QApplication([])

objects_window = uic.loadUi("TCSystem.ui")
objects_window.show()


application.exec()