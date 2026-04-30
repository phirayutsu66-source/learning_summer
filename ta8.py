import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class myApp(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(320, 240)  # กำหนดขนาดหน้าต่าง
        self.setWindowTitle("Hello, World!")  # ชื่อหน้าต่าง

        layout = QVBoxLayout()
        self.setLayout(layout)

        hello = QPushButton("กด!")  # ปุ่ม
        hello.resize(100, 30)

        layout.addWidget(hello)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())