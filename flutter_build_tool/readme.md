# PyQT开发的Flutter工具

**用于批量修改flutter项目中发布时候各种项目中的文件修改**

### 打包命令:
首先输入下面的命令，如果pyinstaller没有下载，请
```
pip install pyinstaller
```
```
pyinstaller -F -w -i flutter.ico main.py
```
或
```
pyinstaller -F -c -i flutter.ico main.py
```

通过CMD命令,build命令  
```
pyinstaller -D main.py
```

C:\workspace\build\main 
main.exe 
查看错误

##### 参数说明：
(建议先用-c，这样如果打包不成功的话可以看到哪里有错）
-F 指只生成一个exe文件，不生成其他dll文件
-w 不弹出命令行窗口
-i 设定程序图标 ，其后面的ico文件就是程序图标main.py 就是要打包的程序
-c 生成的exe文件打开方式为控制台打开。
### 设置打包后的程序icon
flutter packages get
flutter packages pub run flutter_launcher_icons:main
####    启动页
[flutter_native_splash](https://pub.dev/packages/flutter_native_splash)
