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
import time
from shutil import copyfile

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

        f = shelve.open(path+'/db/config.db')
        try:
            if f.__contains__('path'):
               self.label.setText(f['path']['name'])
            if f.__contains__('path_server'):
               self.label_server.setText(f['path_server']['name'])
        finally:
            f.close()


    # 定义槽函数 选择项目根目录
    def checkProject(self):
        directory1 = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        print(directory1)  # 打印文件夹路径
        self.label.setText(directory1)
        path = ''
        if getattr(sys, 'frozen', False):
            # The application is frozen
            path = os.path.dirname(sys.executable)
        else:
            # The application is not frozen
            # Change this bit to match where you store your data files:
            path = os.path.dirname(__file__)
        print(":"+self.label.text()+"/data.txt")
        f = shelve.open(path+'/db/config.db')
        # 写入信息
        try:
            f['path'] = {'name':directory1 }  # 'info'相当于一个键，它的值就是后面保存的字典
        finally:
            f.close()
        # 将保存的信息读取
        # 第一种,直接输出所有内容
    def openServerProject(self):
        directory1 = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        print(directory1)  # 打印文件夹路径
        self.label_server.setText(directory1)
        path = ''
        if getattr(sys, 'frozen', False):
            # The application is frozen
            path = os.path.dirname(sys.executable)
        else:
            # The application is not frozen
            # Change this bit to match where you store your data files:
            path = os.path.dirname(__file__)
        f = shelve.open(path+'/db/config.db')
        # 写入信息
        try:
            f['path_server'] = {'name':directory1 }  # 'info'相当于一个键，它的值就是后面保存的字典
        finally:
            f.close()
        # 将保存的信息读取
        # 第一种,直接输出所有内容

    def openProject(self):
        path=self.label.text()
        os.startfile(path)
    def openServerFolder(self):
        path=self.label_server.text()
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
    def proto2CS(self):
        path = self.label.text()
        #os.system(path+r'\Proto\编译Protoc.bat')
        #subprocess.Popen("cmd.exe /c" + path+r'\Proto\编译Protoc.bat', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #filepath = path+r'\Proto\编译Protoc.bat'
        os.chdir(path+r'\Proto')
        os.startfile("编译Protoc.bat")
        time.sleep(2)
        hotfixMessagePath= path+r'\Unity\Assets\ET.Core\Module\Message\HotfixMessage.cs'
        hotfixOpcodePath=path+r'\Unity\Assets\ET.Core\Module\Message\HotfixOpcode.cs'
        innerMessagePath=path+r'\Unity\Assets\ET.Core\Module\Message\InnerMessage.cs'
        innerOpcodePath=path+r'\Unity\Assets\ET.Core\Module\Message\InnerOpcode.cs'
        outerMessagePath=path+r'\Unity\Assets\ET.Core\Module\Message\OuterMessage.cs'
        outerOpcodePath=path+r'\Unity\Assets\ET.Core\Module\Message\OuterOpcode.cs'
        #####
        pathServer = self.label_server.text()
        hotfixMessageTargetPath=pathServer+'\Server\ET.Core\Module\Message\HotfixMessage.cs'
        copyfile(hotfixMessagePath, hotfixMessageTargetPath)
        hotfixOpcodeTargetPath=pathServer+'\Server\ET.Core\Module\Message\HotfixOpcode.cs'
        copyfile(hotfixOpcodePath, hotfixOpcodeTargetPath)

        innerMessageTargetPath = pathServer + '\Server\ET.Core\Module\Message\InnerMessage.cs'
        copyfile(innerMessagePath, innerMessageTargetPath)
        innerOpcodeTargetPath = pathServer + '\Server\ET.Core\Module\Message\InnerOpcode.cs'
        copyfile(innerOpcodePath, innerOpcodeTargetPath)

        outerMessageTargetPath = pathServer + '\Server\ET.Core\Module\Message\OuterMessage.cs'
        copyfile(outerMessagePath, outerMessageTargetPath)
        outerOpcodeTargetPath = pathServer + '\Server\ET.Core\Module\Message\OuterOpcode.cs'
        copyfile(outerOpcodePath, outerOpcodeTargetPath)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QMainWindow()
    window = mianwindow()
    window.show()
    sys.exit(app.exec_())