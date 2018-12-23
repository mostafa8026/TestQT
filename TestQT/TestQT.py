import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.hellolabel = QLabel('hello world!')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hellolabel)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication()
    widget = MyForm()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
