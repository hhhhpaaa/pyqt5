import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 设置了用于提示框的字体。使用10px大小的SansSerif字体
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)  # 创建按钮组件
        btn.setToolTip('This is a <b>QPushButton</b> widget')  # 为按钮设置提示框
        btn.resize(btn.sizeHint())  # resize()移动按钮，setHint()方法给了按钮一个推荐的大小
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())