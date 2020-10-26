'''
Pyside2 : designer.exe(경로 : venv/Lib/site-packages/Pyside2/designer.exe)를 사용하기위한 모듈

사용법 :     1. designer.exe실행해서 파일 생성(ui파일)
            2. 파일 변환(pycharm) : Terminal접속 - cd명령어로 ui파일이 있는 경로로 가서 ->
                pyuic5 [ui파일이름] -o [생성할 파일 이름]                  ex) testUI.ui / testUI.py
            3. main작성(밑에 예시)
'''
#if __name__ == '__main__':
    #import sys
    #from PyQt5 import QtWidgets
    #app = QtWidgets.QApplication(sys.argv)          #공통
'''    
    Dialog = QtWidgets.QDialog()                    #다이얼로그의 경우
    ui = Ui_Dialog()                                #UI_Dialog()는 클래스명
    ui.setupUi(Dialog)
    Dialog.show()
'''
'''
    MainWindow = QtWidgets.QMainWindow()            #메인윈도우의 경우
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
'''
    #sys.exit(app.exec_())