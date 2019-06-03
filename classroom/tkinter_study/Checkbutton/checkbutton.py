from tkinter import *
w = Tk()
w.title('CheckButton')
w.geometry('500x300')
# 在图形界面上创建一个标签label用以显示并放置
l = Label(w, bg='yellow', width=20, text='empty')
l.pack()


# 定义触发函数功能
def print_selection():
    if (var1.get() == 1) and (var2.get() == 0):
        l.config(text='I love only Python')
    elif (var1.get() == 0) and (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) and (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')


# 定义两个Checkbutton选项并放置
var1 = IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
var2 = IntVar()

c1 = Checkbutton(w,
                 text='Python',
                 variable=var1,
                 onvalue=1,
                 offvalue=0,
                 command=print_selection,
                 cursor='circle',
                 relief=GROOVE)
c1.pack()
c2 = Checkbutton(w,
                 text='C++',
                 variable=var2,
                 onvalue=1,
                 offvalue=0,
                 command=print_selection,
                 cursor='cross',
                 relief=RAISED)
c2.pack()
w.mainloop()
