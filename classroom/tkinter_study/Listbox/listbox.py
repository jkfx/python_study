from tkinter import *

w = Tk()
w.title('listbox study')
w.geometry('500x300')

# 在图形界面上创建一个标签label用以显示并放置
var1 = StringVar()  # 创建变量，用var1用来接收鼠标点击具体选项的内容

l = Label(w,
          bg='green',
          fg='white',
          font=('Arial', 12),
          width=10,
          textvariable=var1)
l.pack()


# 创建一个方法用于按钮的点击事件
def print_selection():
    value = lb.get(lb.curselection())  # 获取当前选中的文本
    var1.set(value)  # 为label设置值


# 创建一个按钮并放置，点击按钮调用print_selection函数
b1 = Button(w,
            text='print selection',
            width=15,
            height=2,
            command=print_selection)
b1.pack()

# 创建Listbox并为其添加内容
var2 = StringVar()
var2.set((1, 2, 3, 4))  # 为变量var2设置值

# 创建Listbox
lb = Listbox(w, listvariable=var2)  # 将var2的值赋给Listbox

# 创建一个list并将值循环添加到Listbox控件中
list_item = [11, 22, 33, 44]
for item in list_item:
    lb.insert('end', item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

w.mainloop()
