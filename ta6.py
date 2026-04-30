import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView


class myWeb(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setHtml('''<html>
<head>
    <title>อิอิ</title>
</head>
<body>
    <h1>Wow!</h1>
    <hr />
    ทดสอบการแสดงผล HTML ใน QWebView
</body>
</html>''')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = myWeb()
    web.show()
    sys.exit(app.exec())