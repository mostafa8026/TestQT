import sys
import random
from PySide2 import QtWidgets, QtCore, QtGui

class MyForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("<font color=red size=30>%s</font>"%"Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)


    def magic(self):
        self.text.setText("<font color=red size=30>%s</font>"%random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    widget = MyForm()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec_())
