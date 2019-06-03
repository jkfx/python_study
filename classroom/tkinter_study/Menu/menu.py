from tkinter import *
w = Tk()
w.title('Menu study')
w.geometry('500x300')
l = Label(w, text='     ', bg='green')
l.pack()
# 定义一个函数功能，用来代表菜单选项的功能，这里为了操作简单，定义的功能比较简单
counter = 0


def do_job():
    global counter
    l.config(text='do ' + str(counter))
    counter += 1


# 创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = Menu(w)
# 创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
filemenu = Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File', menu=filemenu)
# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
# 添加一条分隔线
filemenu.add_separator()
# 用tkinter里面自带的quit()函数
filemenu.add_command(label='Exit', command=w.quit)
# 创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
editmenu = Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为 Edit，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='Edit', menu=editmenu)
# 同样的在 Edit 中加入Cut、Copy、Paste等小命令功能单元
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)
# 创建二级菜单，即菜单项里面的菜单
# 和上面定义菜单一样，不过此处是在File上创建一个空的菜单
submenu = Menu(filemenu)
# 给放入的菜单submenu命名为Import
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
# 创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令
submenu.add_cascade(label='Submenu_1', command=do_job)
# 创建菜单栏完成后，配置让菜单栏menubar显示出来
w.config(menu=menubar)
w.mainloop()
