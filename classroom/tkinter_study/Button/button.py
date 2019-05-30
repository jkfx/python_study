from tkinter import *

w = Tk()  # 实例化objec，建立窗口

w.title('Geek Fx')  # 给窗口的可视化起名字

w.geometry('500x300')  # 设定窗口的大小

# 在图形界面上设定标签
var = StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上

l = Label(w,
          textvariable=var,
          bg='green',
          fg='white',
          font=('Arial', 12),
          width=30,
          height=2)
l.pack()

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')


# 在窗口界面设置放置Button按键
b = Button(w,
           text='hit me',
           font=('Arial', 12),
           width=10,
           height=1,
           command=hit_me)
b.pack()

# 主窗口循环显示
w.mainloop()
