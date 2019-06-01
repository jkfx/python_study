from tkinter import *

w = Tk()
w.title('RadioButton')
w.geometry('500x300')

# 在图形界面上创建一个标签label用以显示并放置
var = StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起
l = Label(w, bg='yellow', width=20, text='empty')
l.pack()


# 定义选项触发函数功能
def print_selection():
    l.config(text='you have selected ' + var.get())


# 创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r1 = Radiobutton(w,
                 text='Option A',
                 variable=var,
                 value='A',
                 command=print_selection)
r1.pack()

r2 = Radiobutton(w,
                 text='Option B',
                 variable=var,
                 value='B',
                 command=print_selection)
r2.pack()
r3 = Radiobutton(w,
                 text='Option C',
                 variable=var,
                 value='C',
                 command=print_selection)
r3.pack()
r4 = Radiobutton(w,
                 text='Option D',
                 variable=var,
                 value='D',
                 command=print_selection)
r4.pack()

w, mainloop()
