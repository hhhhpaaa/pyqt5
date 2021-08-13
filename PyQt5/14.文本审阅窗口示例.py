import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication


class Example(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        title = QLabel('Title')  # 创建标题
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()  # 创建单行编辑框
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()  # 创建文本编辑框

        grid = QGridLayout()  # 创建网格布局
        grid.setSpacing(10)  # 设置了组件之间的间距

        grid.addWidget(title, 1, 0)  # 对应坐标位置将标题添加到网格布局中
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)  # 对应坐标位置将文本编辑框添加到网格布局中， 让其跨越5行，跨越1列

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())