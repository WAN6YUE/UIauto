import os.path
import sys
#os模块是和操作系统交互相关模块
import pythonTwo

pythonTwo.sayhi()
print(sys.path)

print(__file__) #打印当前脚本文件路径
print(os.path.dirname(os.path.dirname(__file__)))#os.path.dirname 去掉路径最后一个文件或者目录 获得新的目录名称