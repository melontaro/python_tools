import sys
from ui.MainWindow import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class mianwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mianwindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数 选择项目根目录
    def chooseRootDir(self):
        directory1 = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        print(directory1)  # 打印文件夹路径
        self.label.setText(directory1)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QMainWindow()
    window = mianwindow()
    window.show()
    sys.exit(app.exec_())