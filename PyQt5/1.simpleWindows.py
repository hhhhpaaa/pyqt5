import sys
from PyQt5.QtWidgets import QApplication, QWidget  # 声明PyQt5.QtWidgets模块，这个模块包含了基本的组件


if __name__ == '__main__':

    # sys.argv是一组命令行参数的列表。Python可以在shell里运行，这个参数提供对脚本控制的功能。
    app = QApplication(sys.argv)  # 每个PyQt5应用都必须创建一个应用对象

    # QWidget控件是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口window）。
    w = QWidget()
    w.resize(250, 150)  # 改变控件的大小(宽,高)
    # move()是修改控件位置的的方法。它把控件放置到屏幕坐标的(300,300)的位置。注：屏幕坐标系的原点是屏幕的左上角。
    w.move(300, 300)
    # 添加标题
    w.setWindowTitle('Simple')
    w.show()  # 显示
    # exit() 方法销毁主控件，主循环就会结束. sys.exit() 方法能确保主循环安全退出
    sys.exit(app.exec_())  # app.exec_()运行主循环，并在退出时返回状态代码
