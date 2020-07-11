#  /**
#   * // +----------------------------------------------------------------------
#   * // | XamClub [ WE CAN DO IT MORE SIMPLE ]
#   * // +----------------------------------------------------------------------
#   * // | Copyright (c) 2013-2020 http://www.xamclub.com All rights reserved.
#   * // +----------------------------------------------------------------------
#   * // | Licensed ( http://www.apache.org/licenses/LICENSE-2.0 )
#   * // +----------------------------------------------------------------------
#   * // | Author: TouchAfflatus <axuyin@163.com>
#   * // +----------------------------------------------------------------------
#   */

import sys
import shelve
from ui.MainWindow import *
from PyQt5.QtWidgets import QFileDialog
import os


class mianwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mianwindow, self).__init__()
        self.setupUi(self)
        path =''
        if getattr(sys, 'frozen', False):
            # The application is frozen
            path = os.path.dirname(sys.executable)
        else:
            # The application is not frozen
            # Change this bit to match where you store your data files:
            path = os.path.dirname(__file__)

        os.path.dirname(path)#__file__
        f = shelve.open(path+'/db/config.db')
        if f.__contains__('path'):
           print('path is not none')
           self.label.setText(f['path']['name'])


    # 定义槽函数 选择项目根目录
    def checkProject(self):
        directory1 = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        print(directory1)  # 打印文件夹路径
        self.label.setText(directory1)
        path = os.path.dirname(__file__)
        print(":"+self.label.text()+"/data.txt")
        f = shelve.open(path+'/db/config.db')
        # 写入信息
        f['path'] = {'name':directory1 }  # 'info'相当于一个键，它的值就是后面保存的字典
        # 将保存的信息读取
        # 第一种,直接输出所有内容
        print(f['path'])

    def openProject(self):
        path=self.label.text()
        os.startfile(path)
    def openHotfixMessage(self):
        path = self.label.text()
        print(path)
        file=path+r'/Proto/HotfixMessage.proto'
        print(file)
        os.startfile(file)

    def openInnerMessage(self):
        path = self.label.text()
        file=path+r'\Proto\InnerMessage.proto'
        os.startfile(file)
    def openOuterMessage(self):
        path = self.label.text()
        os.startfile(path+r'\Proto\OuterMessage.proto')


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QMainWindow()
    window = mianwindow()
    window.show()
    sys.exit(app.exec_())