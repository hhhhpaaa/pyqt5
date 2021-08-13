import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PyQt5.QtGui import QColor


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        col = QColor(0, 0, 0)  # 初始化QtGuiQFrame组件的背景颜色

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)  # 事件槽连接到showDialog，如果点击该事件就会执行

        self.frm = QFrame(self)  # 创建QFrame组件
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())  # 设置颜色
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):

        # 弹出颜色选择框
        col = QColorDialog.getColor()

        # 选中一个颜色并且点了ok按钮，会返回一个有效的颜色值。
        # 如果点击了Cancel按钮，不会返回选中的颜色值。使用样式表来定义背景颜色。
        if col.isValid():

            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())