import sys

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('Hello World')
# w.setGeometry(100,200,300,400)
app.setWindowIcon(QIcon('./img/IDB_ICON_EXCLAMATION.bmp'))

btn1 = QPushButton('Button' ,w)
btn1.setGeometry(100,100,100,100)
btn1.resize(btn1.sizeHint())
btn1.setToolTip('QT버튼')

w.show()

sys.exit(app.exec())