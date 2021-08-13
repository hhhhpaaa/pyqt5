import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        self.btn = QPushButton('Dialog', self)  # 创建按钮
        self.btn.move(20, 20)  # 移动按钮
        self.btn.clicked.connect(self.showDialog)  # 将showDialog事件连接到按钮点击的事件槽中
        self.le = QLineEdit(self)  # 创建单行文本输入框
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):

        # 创建一个输入对话框。第一个字符串参数是对话框的标题，第二个字符串参数是对话框内的消息文本。对话框返回输入的文本内容和一个布尔值。
        # 如果我们点击了Ok按钮，布尔值就是true，反之布尔值是false（译者注：也只有按下Ok按钮时，返回的文本内容才会有值）
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        #  如果为真， 将对话框内容设置为输入内容
        if ok:

            self.le.setText(str(text))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())