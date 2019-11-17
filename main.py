import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(100, 100)
        self.btn.move(100, 100)
        self.label = QLabel(self)
        self.label.move(80, 30)
        self.btn.clicked.connect(self.run)

    def run(self):
        self.pixmap = QPixmap('Безымянный.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(500, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())