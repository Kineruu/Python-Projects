from PyQt6.QtWidgets import QApplication, QLabel,  QWidget

import sys


app = QApplication([])

window = QWidget()
window.setWindowTitle("Hello")
window.setGeometry(50,50,1800,500)

label = QLabel("Hello", parent=window)
anotherlabel = QLabel("<h4>WAIT I CAN USE HTML AS WELL????????</h4>", parent=window)

window.show()

app.exec()