import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()

		self.setGeometry(50, 50, 500, 500)
		self.setWindowTitle("Programa de facturacion")
		self.home()

	def home(self):
		button= QtGui.QPushButton("Salir", self)
		button.clicked.connect(self.close_application)
		button.resize(button.minimumSizeHint())
		button.move(0, 0)
		self.show()

	def close_application(self):
		sys.exit()


app = QtGui.QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())