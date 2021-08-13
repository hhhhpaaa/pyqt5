import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        # QAction是一个用于菜单栏、工具栏或自定义快捷键的抽象动作行为
        exitAction = QAction(QIcon('pycharm.ico'), '&Exit', self)  # 创建了一个视觉(动作)，并添加了图标和标签
        exitAction.setShortcut('Ctrl+Q')  # 设置快捷方式
        exitAction.setStatusTip('Exit application')  # 设置提示信息，将会在状态栏显示
        # 选中特定的动作，一个触发信号会被发射。信号连接到QApplication组件的quit()方法。这样就中断了应用
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()  # 创建状态栏

        menubar = self.menuBar()  # 创建菜单栏
        fileMenu = menubar.addMenu('&File')  # 创建一个file菜单
        fileMenu.addAction(exitAction)  # 将退出动作添加到file菜单中

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())