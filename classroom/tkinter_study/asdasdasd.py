from tkinter import *

# 初始化窗口
root = Tk()
root.geometry('300x350')
root.title('GeekFx')
root.resizable(width=False, height=False)

# Label窗口
l = Label(root, text='')
l.pack()

# Menu菜单
counter = 0
def do_job():
    global counter
    counter += 1
    #l.config(text='do ' + str(counter))

# 菜单容器
menubar = Menu(root)
# first菜单
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='标准', menu=filemenu)
filemenu.add_command(label='计算器', command=do_job)
filemenu.add_command(label='---标准', command=do_job)
filemenu.add_command(label='---科学', command=do_job)
filemenu.add_command(label='---日期计算', command=do_job)
filemenu.add_separator()    # 添加一条分隔线
filemenu.add_command(label='转换器', command=do_job)
filemenu.add_command(label='---货币', command=do_job)
filemenu.add_command(label='---长度', command=do_job)
filemenu.add_command(label='---重量', command=do_job)
filemenu.add_separator()  # 添加一条分隔线
filemenu.add_command(label='退出', command=root.quit)
# secound 菜单
helpmenu = Menu(root, tearoff=0)
menubar.add_cascade(label='帮助', menu=helpmenu)
helpmenu.add_command(label='查看帮助', command=do_job)
helpmenu.add_separator()
helpmenu.add_command(label='关于计算器', command=do_job)
root.config(menu=menubar)  # 创建菜单栏完成后，配置让菜单栏menubar显示出来

t = Text(root, width=42, height=10)
t.place(x=0, y=0)

b = Button(root, width=2, height=0)
b.place(x=0,y=160)
root.mainloop()
