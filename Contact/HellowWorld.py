import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon


class HelloWorld(QWidget):

    def __init__(self):
        super().__init__()
        self.buttonUI()
        self.initUI()

    def buttonUI(self):

        btn = QPushButton('Button',self)
        btn.setToolTip('QT 버튼')
        btn.resize(btn.sizeHint())
        btn.move(100,100)

    def initUI(self):

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Hello World')
        self.show()

app = QApplication(sys.argv)
exe = HelloWorld()
app.setWindowIcon(QIcon('./img/IDB_ICON_EXCLAMATION.bmp'))

sys.exit(app.exec())
