import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("bottle Website")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowIcon(QIcon("plastic_bottle.jpg"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()