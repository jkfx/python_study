from tkinter import *

w = Tk()
w.title('text study')
w.geometry('500x300')

# 在图形界面上设定输入框控件entry框并放置
e = Entry(w, show=None)
e.pack()


# 定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def inser_point():  # 在鼠标焦点处插入输入内容
    var = e.get()
    t.insert('insert', var)


def insert_end():
    var = e.get()
    t.insert('end', var)


# 创建并放置两个按钮分别触发两种情况
b1 = Button(w, text='insert point', width=10, height=2, command=inser_point)
b1.pack()
b2 = Button(w, text='insert_end', width=10, height=2, command=insert_end)
b2.pack()

# 创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t = Text(w, height=3)
t.pack()

w.mainloop()
