from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
import random
import sys

print(PySide6.__version__)
print(PySide6.QtCore.__version__)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hello", "Hi", "Good morning", "Good evening"]

        self.button = QtWidgets.QPushButton("Click here!")
        self.text = QtWidgets.QLabel("Hello!!!!", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = MyWidget()
    widget.resize(600, 600)
    widget.show()

    sys.exit(app.exec())