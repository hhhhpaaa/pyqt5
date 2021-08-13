import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)  # 创建数字数码管
        sld = QSlider(Qt.Horizontal, self)  # 创建水平滑动块

        vbox = QVBoxLayout()  # 创建箱布局
        vbox.addWidget(lcd)  # 添加数码管到箱布局
        vbox.addWidget(sld)

        self.setLayout(vbox)  # 添加箱布局到窗口
        sld.valueChanged.connect(lcd.display)  # 将滑块条的valueChanged信号和lcd数字显示的display槽连接在一起

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())