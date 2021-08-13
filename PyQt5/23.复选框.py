import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self)  # 创建复选框，用来切换窗口标题
        cb.move(20, 20)
        cb.toggle()  # 选中复选框
        cb.stateChanged.connect(self.changeTitle)  # 将事件槽连接到changeTitle，并传入参数

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    # 复选框组件的状态会传入changeTitle()方法的state参数
    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())