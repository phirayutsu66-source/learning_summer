import sys
from PySide6.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(320, 240)  # กำหนดขนาดหน้าต่าง
        self.setWindowTitle("Hello, World!")  # ชื่อโปรแกรม

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Hello World")
        label2 = QLabel("สวัสดี")
        label3 = QLabel("เพิ่งเริ่มต้นเรียน PySide6")

        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec())