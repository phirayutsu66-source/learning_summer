import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox


class myMessageBox(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('กล่องข้อความ')  # ชื่อหน้าต่าง

    # ดักตอนกดปิดหน้าต่าง
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Message',
            "คุณแน่ใจนะว่าคุณต้องการปิดโปรแกรม?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()   # ปิด
        else:
            event.ignore()   # ไม่ปิด


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qb = myMessageBox()
    qb.show()
    sys.exit(app.exec())