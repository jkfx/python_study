import os
import tkinter
import tkinter.messagebox

libs = set()


# 选择是否安装的库
def select(var, lib):
    if var.get():
        libs.add(lib)
    else:
        libs.discard(lib)


# 开始安装选择的库
def install():
    try:
        # 安装前更新下pip
        os.system('python -m pip install --upgrade pip')
        for lib in libs:
            os.system('pip install ' + lib)
        tkinter.messagebox.showinfo(title='安装完成',
                                    message='安装完毕，使用"pip list"查看安装成功的库')
    except:
        tkinter.messagebox.showerror(title='安装失败',
                                     message='因为某些原因失败，具体查看端口窗口的提示')


def create_checkbutton(self, name1, name2, name3, name4):
    button_frame = tkinter.Frame(self)
    button_frame.pack()
    var1 = tkinter.IntVar()
    var2 = tkinter.IntVar()
    tkinter.Checkbutton(button_frame,
                        variable=var1,
                        text=name1,
                        command=lambda: select(var1, name3)).pack(side='left')
    tkinter.Checkbutton(button_frame,
                        variable=var2,
                        text=name2,
                        command=lambda: select(var2, name4)).pack(side='right')


def select_set(main_frame):
    create_checkbutton(main_frame, 'NumPy', 'Matplotlib', 'numpy',
                       'matplotlib')
    create_checkbutton(main_frame, 'PIL', 'Scikit-Learn', 'pillow', 'sklearn')
    create_checkbutton(main_frame, 'Requests', 'Beautiful Soup', 'requests',
                       'beautifulsoup4')
    create_checkbutton(main_frame, 'Wheel', 'PyInstaller', 'wheel',
                       'pyinstaller')
    create_checkbutton(main_frame, 'Jieba', 'Django', 'jieba', 'django')
    create_checkbutton(main_frame, 'Flask', 'WeRoBot', 'flask', 'werobot')
    create_checkbutton(main_frame, 'SymPy', 'Pandas', 'sympy', 'pandas')
    create_checkbutton(main_frame, 'Networkx', 'PyQt5', 'networkx', 'pyqt5')
    create_checkbutton(main_frame, 'PyOpenGL', 'PyPDF2', 'pyopengl', 'pypdf2')
    create_checkbutton(main_frame, 'Docopt', 'PyGame', 'docopt', 'pygame')


def main_graphical():
    root = tkinter.Tk()
    root.title('Python third party library installation')
    root.geometry('500x400')
    # 主Frame
    main_frame = tkinter.Frame(root)
    main_frame.pack()
    # 在主Frame上显示Label
    frame_label = tkinter.Frame(main_frame)
    frame_label.pack(anchor='n')
    label_top = tkinter.Label(frame_label, text='\nPython第三方库在线安装程序\n')
    label_top.pack(anchor='n')
    # 在主Frame上添加所有第三方库的选项按钮
    select_set(main_frame)
    # 安装、退出按钮
    install_quit_frame = tkinter.Frame(main_frame)
    install_quit_frame.pack()
    tkinter.Button(install_quit_frame, text='安装', width=6,
                   command=install).pack(side='left')
    tkinter.Button(install_quit_frame, text='退出', width=6,
                   command=root.quit).pack(side='right')

    root.mainloop()


main_graphical()
