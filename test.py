'''Tkinter教程之Message篇'''
# Message也是用来显示文本的，用法与Label基本一样
'''1.创建一个简单的Message'''
from tkinter import *

root = Tk()
# 运行程序，可以看到Hello之后，Message显示在它的下一行，这也是Message的一个特性。Label没有。
Message(root, text='hello Message').pack()

'''2.如果不让它换行的话，指定足够大的宽度'''
Message(root, text='hello Message', width=100).pack()

'''3.使用aspect属性指定宽高比例'''
for i in range(10):
    Message(root, text='A' * i, aspect=400).pack()
root.mainloop()