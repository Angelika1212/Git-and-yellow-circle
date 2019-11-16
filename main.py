import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.pixmap = QPixmap('Безымянный.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(500, 500)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())