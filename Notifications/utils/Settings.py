from PySide6 import QtCore, QtWidgets
import json
import os

class Settings(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        self.ConfigPath = os.path.join(self.BASE_PATH, "..", "config.json")
        self.ConfigPath = os.path.abspath(self.ConfigPath) 
        with open(self.ConfigPath, "r") as f:
            self.config = json.load(f)

        self.init_ui()

        self.setFixedSize(self.sizeHint())
    
    def init_ui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Settings")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.customSize = QtWidgets.QCheckBox("Custom size?", self)
        self.setCursor(QtCore.Qt.PointingHandCursor)

        def checkState():
            if self.customSize.isChecked():
                self.config["CUSTOMSIZE"] = "YES"
            else:
                self.config["CUSTOMSIZE"] = "NO"
            with open(self.ConfigPath, "w") as f:
                json.dump(self.config, f, indent=4)

        self.customSize.stateChanged.connect(checkState)

        # Create layout and other stuff
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.customSize)
        self.setLayout(self.layout)


    