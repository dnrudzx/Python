'''
PyQt5 : 파이썬 GUI프로그래밍을 위한 모듈
    패키지 설치 :    PyQt5 : GUI프로그래밍을 위한 모듈
                   Pyside2 : 설치하면 Qt Designer 사용 가능(경로 : venv/Lib/site-packages/Pyside2/designer.exe)
'''
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('기본 타이틀')
        self.setGeometry(300,300,300,150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
