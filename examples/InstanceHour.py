#coding:utf-8
from jpype import *

#demo1 打印hello world
startJVM(getDefaultJVMPath())
java.lang.System.out.println("hello world")
shutdownJVM()

