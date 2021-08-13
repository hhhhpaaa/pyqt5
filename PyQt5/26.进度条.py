import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)  # 构造滑块条
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)  # 创建按钮
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)  # 将按钮触发连接到doAction

        self.timer = QBasicTimer()  # 用定时器对象来激活进度条
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    # timerEvent()事件处理函数用于处理定时事件
    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    # 开始停止计数器
    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            # 开启定时器事件调用了start()方法。
            # 这个方法有两个参数：定时时间和接收定时器事件的对象。
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())