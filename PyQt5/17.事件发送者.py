import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):

        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        btn1 = QPushButton('Button 1', self)
        btn1.move(30, 50)

        btn2 = QPushButton('Button 2', self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)  # 两个按钮都连接到了同一个槽中
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()  # 创建状态栏

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):

        sender = self.sender()  # 调用sender()方法判断发送信号的信号源
        self.statusBar().showMessage(sender.text() + 'was pressed')  # 状态栏显示信息

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
