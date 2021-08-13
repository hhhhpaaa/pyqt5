import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, qApp, QWidget, QMessageBox
from PyQt5.QtGui import QIcon


class Example(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()  # 创建文本编辑框组件
        self.setCentralWidget(textEdit)  # 添加文本编辑框组件

        exitAction = QAction(QIcon('pycharm.ico'), 'Exit', self)  # 创建了一个视觉(动作)，并添加了图标和标签
        exitAction.setShortcut('Ctrl+Q')  # 设置快捷方式
        exitAction.setStatusTip('Exit application')  # 设置提示信息，将会在状态栏显示
        # 选中特定的动作，一个触发信号会被发射。信号连接到QApplication组件的quit()方法。这样就中断了应用
        exitAction.triggered.connect(qApp.quit)
        # exitAction.triggered.connect(self.close)

        self.statusBar().showMessage('hhhhh')  # 创建状态栏并显示信息

        menubar = self.menuBar()  # 创建菜单栏
        fileMenu = menubar.addMenu('&File')  # 创建一个file菜单
        fileMenu.addAction(exitAction)  # 将退出动作添加到file菜单中

        toolbar = self.addToolBar('Exit')  # 创建工具栏
        toolbar.addAction(exitAction)  # 将退出动作添加到工具栏

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()

    def closeEvent(self, event):

        #  关闭一个QWidget，QCloseEvent类事件将被生成。要修改组件动作重新实现closeEvent()事件处理方法
        #  代码中第一个字符串的内容被显示在标题栏上。第二个字符串是对话框上显示的文本。
        #  第三个参数指定了显示在对话框上的按钮集合。最后一个参数是默认选中的按钮。这个按钮一开始就获得焦点。返回值被储存在reply变量中
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()  # 接受
        else:
            event.ignore()  # 取消


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())