import sys
from PySide6.QtWidgets import *

app = QApplication(sys.argv)

label = QLabel("<font color=red size=40>Hello World</font>")
label.resize(320, 240)
label.setWindowTitle("Hello, World!")
label.show()

sys.exit(app.exec())