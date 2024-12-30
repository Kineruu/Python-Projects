from PySide6 import QtCore, QtWidgets

class Error(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()    
        self.init_ui()

        self.setFixedSize(self.sizeHint())
    
    def init_ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Error occured. Please check if all the fields are filled correctly. \nIf the error is code related, please DM me on Discord.")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.OKButton = QtWidgets.QPushButton(self)
        self.OKButton.setText("OK")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.OKButton.clicked.connect(self.close)

        # Create layout and other stuff
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.OKButton)
        self.setLayout(self.layout)
    