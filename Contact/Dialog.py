import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("Gui.ui")[0]

class DialogWindow(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self,"Message","버튼 클릭")
        self.label.setText("버튼클릭")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = DialogWindow()
    dialog.show()
    app.exec_()