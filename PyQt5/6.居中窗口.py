import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
#  QtGui.QDesktopWidget类提供了我们桌面窗口的信息，包含了屏幕尺寸


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):

        qr = self.frameGeometry()
        #  获得主窗口的一个矩形特定几何图形。包含了窗口的框架。
        cp = QDesktopWidget().availableGeometry().center()
        #  算出相对于显示器的绝对值。并且从这个绝对值中，获得了屏幕中心点
        qr.moveCenter(cp)
        #  把矩形的中心设置到屏幕的中间去。矩形的大小并不会改变。
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())