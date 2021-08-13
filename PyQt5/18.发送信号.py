import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


#  信号使用了pyqtSignal()方法创建，并且成为外部类Communicate类的属性
class Communicate(QObject):

    closeApp = pyqtSignal()


#  创建一个新的信号叫做closeApp。
#  当触发鼠标点击事件时信号会被发射。信号连接到了QMainWindow的close()方法。
class Example(QMainWindow):

    def __init__(self):

        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        #  把自定义的closeApp信号连接到QMainWindow的close()槽上
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    #  在窗口上点击一下鼠标，closeApp信号会被发射。应用中断。
    def mousePressEvent(self, event):

        self.c.closeApp.emit()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())