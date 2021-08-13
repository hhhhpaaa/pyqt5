import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()  # 创建网格布局
        self.setLayout(grid)  # 添加网格布局到主窗口

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]  # 创建坐标列表

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)  # 添加按钮
            grid.addWidget(button, *position)  # 将按钮按坐标位置添加到网格布局中

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())