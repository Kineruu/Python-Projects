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

        self.customTitles = QtWidgets.QCheckBox("Custom titles?", self)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.customTitles.setCheckState(QtCore.Qt.Checked if self.config["CUSTOMTITLES"] == "YES" else QtCore.Qt.Unchecked)

        def checkState():
            if self.customTitles.isChecked():
                self.config["CUSTOMTITLES"] = "YES"
            else:
                self.config["CUSTOMTITLES"] = "NO"
            with open(self.ConfigPath, "w") as f:
                json.dump(self.config, f, indent=4)
        
        self.customTitles.stateChanged.connect(checkState)



        self.customSize = QtWidgets.QCheckBox("Custom size?", self)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        self.customSize.setCheckState(QtCore.Qt.Checked if self.config["CUSTOMSIZE"] == "YES" else QtCore.Qt.Unchecked)

        def checkState():
            if self.customSize.isChecked():
                self.config["CUSTOMSIZE"] = "YES"
            else:
                self.config["CUSTOMSIZE"] = "NO"
            with open(self.ConfigPath, "w") as f:
                json.dump(self.config, f, indent=4)

        self.customSize.stateChanged.connect(checkState)

        self.heightBox = QtWidgets.QLineEdit(self)
        self.heightBox.setPlaceholderText("Height")
        self.heightBox.setFixedSize(125, 35)
        self.heightBox.setText(str(self.config["HEIGHT"]))
        self.heightBox.setEnabled(True if self.config["CUSTOMSIZE"] == "YES" else False)
        
        self.widthBox = QtWidgets.QLineEdit(self)
        self.widthBox.setPlaceholderText("Width")
        self.widthBox.setFixedSize(125, 35)
        self.widthBox.setText(str(self.config["WIDTH"]))
        self.widthBox.setEnabled(True if self.config["CUSTOMSIZE"] == "YES" else False)

        def getSizes():
            if self.customSize.isChecked():
                self.config["HEIGHT"] = int(self.heightBox.text())
                self.config["WIDTH"] = int(self.widthBox.text())
                with open(self.ConfigPath, "w") as f:
                    json.dump(self.config, f, indent=4)
        
        self.heightBox.textChanged.connect(getSizes)

        # Create layout and other stuff
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.customTitles)
        self.layout.addWidget(self.customSize)
        self.layout.addWidget(self.heightBox)
        self.layout.addWidget(self.widthBox)
        self.setLayout(self.layout)


    