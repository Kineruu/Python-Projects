from PySide6 import QtCore, QtWidgets

class Settings(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()    
        self.init_ui()

        self.setFixedSize(self.sizeHint())
    
    def init_ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Settings")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.customSize = QtWidgets.QCheckBox("Custom size?", self)
        self.setCursor(QtCore.Qt.PointingHandCursor)

        # Create layout and other stuff
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.customSize)
        self.setLayout(self.layout)


    