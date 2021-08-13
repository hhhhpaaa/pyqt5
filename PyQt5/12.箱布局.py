import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton("OK")  # 创建按钮
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()  # 创建水平箱布局
        hbox.addStretch(1)  # 增加了一个拉伸因子
        hbox.addWidget(okButton)  # 添加按钮
        hbox.addWidget(cancelButton)

        # addWidget()方法用于向布局中添加控件
        # addLayout()方法用于向布局中添加子布局

        vbox = QVBoxLayout()  # 创建垂直箱布局
        vbox.addStretch(1)  # 增加了一个拉伸因子
        vbox.addLayout(hbox)  # 将水平布局添加到垂直布局内

        self.setLayout(vbox)  # 将布局添加到主窗口

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())