import sys
from PySide2.QtWidgets import QApplication, QWidget,QPushButton, QLabel
#from PySide2 import QtCore
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(1000, 500)
    w.setWindowTitle("Hello Pyside")
    btn = QPushButton('Quit', w)
    btn.move(100, 50)
   # btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
    label = QLabel("Hello", w)
    label.setGeometry(100, 100, 200, 100)
    btn.clicked.connect(lambda : label.setText("World"))

    w.show()

    app.exec_()