import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtGui import QFont


app = QApplication(sys.argv)

quit_btn = QPushButton("ออก")  # ตั้งชื่อไม่ให้ชนกับคำว่า quit
quit_btn.resize(75, 30)
quit_btn.setFont(QFont("Times", 18, QFont.Bold))

# แบบใหม่ (สำคัญ)
quit_btn.clicked.connect(app.quit)

quit_btn.show()

sys.exit(app.exec())