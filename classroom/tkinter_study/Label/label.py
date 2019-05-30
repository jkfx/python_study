from tkinter import *

w = Tk()  # 实例化object，建立窗口

w.title('Geek Fx')  # 给窗口的可视化起名字

w.geometry('500x300')  # 设定窗口的大小

# 在图形界面上设定标签
l = Label(
    w,
    text='你好！this is Tkinter',
    bg='green',  # bg 为背景
    font=('Arial', 12),  # font 为字体
    width=30,  # width 为长
    height=2  # height 为高
    # 这里长和高时字符的长和高，比如 height=2 就是标签有2个字符这么高
)

# 放置标签
l.pack()  # Label 内容的content区域放置位置，自动调节尺寸
# 放置的方法有：1）l.pack() 2）l.place()

# 主窗口循环显示
w.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
