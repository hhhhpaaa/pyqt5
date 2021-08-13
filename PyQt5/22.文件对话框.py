import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.textEdit = QTextEdit()  # 创建多行文本框控件
        self.setCentralWidget(self.textEdit)  # 设置为中心窗口
        self.statusBar()  # 创建状态栏

        openFile = QAction(QIcon('pycharm.ico'), 'Open', self)  # 创建了一个事件(动作)，并添加了图标和标签
        openFile.setShortcut('Ctrl+O')  # 设置快捷键
        openFile.setStatusTip('Open new File')  # 设置提示信息，显示在状态栏
        openFile.triggered.connect(self.showDialog)  # 将事件槽连接到showDialog，鼠标点击时启动showDialog

        menubar = self.menuBar()  # 设置菜单栏
        fileMenu = menubar.addMenu('&File')  # 添加file菜单
        fileMenu.addAction(openFile)  # 为file菜单添加控件

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):

        # 弹出文件选择框。第一个字符串参数是getOpenFileName()方法的标题。
        # 第二个字符串参数指定了对话框的工作目录和文件名。默认的，文件过滤器设置成All files (*)。
        # 返回值为('C:/Users/hhhhpaa/Desktop/SHT20.txt', 'All Files (*)')， 文件路径和过滤器类型
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:/')

        # 读取文件， 写入多行文本控件
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())