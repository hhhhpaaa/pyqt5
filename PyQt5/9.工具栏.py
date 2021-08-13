import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('pycharm.ico'), 'Exit', self)  # 创建了一个事件(动作)，并添加了图标和标签
        exitAction.setShortcut('Ctrl+Q')  # 设置快捷方式
        # 选中特定的动作，一个触发信号会被发射。信号连接到QApplication组件的quit()方法。这样就中断了应用
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')  # 创建工具栏
        self.toolbar.addAction(exitAction)  # 将退出动作添加到工具栏

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())