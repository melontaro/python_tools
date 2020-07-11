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
from ui.MainWindow import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import webbrowser
import shutil
import re
import json

class mianwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mianwindow, self).__init__()
        self.setupUi(self)



    # 定义槽函数 选择项目根目录
    def chooseRootDir(self):
        directory1 = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
        print(directory1)  # 打印文件夹路径
        self.label.setText(directory1)
        print(":"+self.label.text()+"/data.txt")
        webbrowser.open_new("https://flutter.dev/docs/deployment/android")
    def copykeytoandroiddir(self):
        flutterpath=self.label.text()
        androidpath=flutterpath+"/android"
        keyfilepath="config/key.jks"
        keyproperties="config/key.properties"
        shutil.copyfile(keyfilepath,androidpath+"/key.jks")
        shutil.copyfile(keyproperties, androidpath + "/key.properties")

    def replaceContent(self):
        self.replacebuildgradle_android()
        self.replacebuildgradle_buildTypes()
        self.replacebuildgradle_ndk()
        self.replacebuildgradle_minsdkversion()
        self.replace_appname()


    #replace android/app/build.gradle file
    def replacebuildgradle_android(self):
        flutterpath = self.label.text()
        buildgradlepath = flutterpath + "/android/app/build.gradle"

        # read input file
        fin = open(buildgradlepath, "rt")
        # read file contents to string
        data = fin.read()
        # replace all occurrences of the required string
        strinfo = re.compile('android {')

        str1 = """def keystoreProperties = new Properties()
def keystorePropertiesFile = rootProject.file('key.properties')
if (keystorePropertiesFile.exists()) {
keystoreProperties.load(new FileInputStream(keystorePropertiesFile))
}

android {"""

        data = strinfo.sub(str1, data)
        # close the input file
        fin.close()
        # open the input file in write mode
        fin = open(buildgradlepath, "wt")
        # overrite the input file with the resulting data
        fin.write(data)
        # close the file
        fin.close()
        return
    def replacebuildgradle_buildTypes(self):
        flutterpath = self.label.text()
        buildgradlepath = flutterpath + "/android/app/build.gradle"

        # read input file
        fin = open(buildgradlepath, "rt")
        # read file contents to string
        data = fin.read()
        # replace all occurrences of the required string
        compileStr="""    buildTypes {
        release {
            // TODO: Add your own signing config for the release build.
            // Signing with the debug keys for now, so `flutter run --release` works.
            signingConfig signingConfigs.debug
        }
    }"""
        strinfo = re.compile(compileStr)

        str1 = """signingConfigs {
       release {
           keyAlias keystoreProperties['keyAlias']
           keyPassword keystoreProperties['keyPassword']
           storeFile keystoreProperties['storeFile'] ? file(keystoreProperties['storeFile']) : null
           storePassword keystoreProperties['storePassword']
       }
   }
   buildTypes {
       release {
           signingConfig signingConfigs.release
       }
   }
"""

        data = strinfo.sub(str1, data)
        # close the input file
        fin.close()
        # open the input file in write mode
        fin = open(buildgradlepath, "wt")
        # overrite the input file with the resulting data
        fin.write(data)
        # close the file
        fin.close()
        return
    def replacebuildgradle_ndk(self):
        flutterpath = self.label.text()
        buildgradlepath = flutterpath + "/android/app/build.gradle"

        # read input file
        fin = open(buildgradlepath, "rt")
        # read file contents to string
        data = fin.read()
        # replace all occurrences of the required string
        compileStr="""        versionName flutterVersionName"""
        strinfo = re.compile(compileStr)

        str1 = """        versionName flutterVersionName
        ndk{
            abiFilters "armeabi-v7a"
        }
"""
        data = strinfo.sub(str1, data)
        # close the input file
        fin.close()
        # open the input file in write mode
        fin = open(buildgradlepath, "wt")
        # overrite the input file with the resulting data
        fin.write(data)
        # close the file
        fin.close()
        return

    def replacebuildgradle_minsdkversion(self):
            flutterpath = self.label.text()
            buildgradlepath = flutterpath + "/android/app/build.gradle"

            # read input file
            fin = open(buildgradlepath, "rt")
            # read file contents to string
            data = fin.read()
            # replace all occurrences of the required string
            compileStr = """minSdkVersion.*"""
            strinfo = re.compile(compileStr)

            str1 = """minSdkVersion 19"""
            data = strinfo.sub(str1, data)
            # close the input file
            fin.close()
            # open the input file in write mode
            fin = open(buildgradlepath, "wt")
            # overrite the input file with the resulting data
            fin.write(data)
            # close the file
            fin.close()
            return
    def replace_appname(self):
            configinfo=None
            with open("config/config.json", 'r') as f:
                configinfo = json.loads(f.read())
            appname=configinfo['appname']
            flutterpath = self.label.text()
            mainfestpath = flutterpath + "/android/app/src/main/AndroidManifest.xml"

            # read input file
            fin = open(mainfestpath, "rt")
            # read file contents to string
            data = fin.read()
            # replace all occurrences of the required string
            compileStr = """        android:label=.*"""
            strinfo = re.compile(compileStr)

            str1 = """        android:label=\""""+appname+'\"'
            data = strinfo.sub(str1, data)
            # close the input file
            fin.close()
            # open the input file in write mode
            fin = open(mainfestpath, "wt")
            # overrite the input file with the resulting data
            fin.write(data)
            # close the file
            fin.close()
            return

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QMainWindow()
    window = mianwindow()
    window.show()
    sys.exit(app.exec_())