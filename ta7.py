import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView


class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()

        # อ่านไฟล์รูป (เช่น image.png)
        with open("Untitled-1.png", "rb") as f:
            img = f.read()

        # แสดงรูปใน QWebEngineView
        self.setContent(img, "image/png")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = myWeb()
    web.show()
    sys.exit(app.exec())