import os
import tkinter
import tkinter.messagebox

libs = set()


def select(var, lib):
    if var.get():
        libs.add(lib)
    else:
        libs.discard(lib)


def install():
    try:
        os.system('python -m pip install --upgrade pip')
        for lib in libs:
            os.system('pip install ' + lib)
        tkinter.messagebox.showinfo(title='安装成功', message='安装成功!')
    except:
        tkinter.messagebox.showerror(title='安装失败',
                                     message='安装失败，请使用"pip list"查看安装了那些库')


def graphical():
    window = tkinter.Tk()
    window.geometry('600x400')
    window.title('Python third party library installation')

    # 总frame
    frame = tkinter.Frame(window)
    frame.pack()
    # 在上层显示标签
    frame_label = tkinter.Frame(frame)
    frame_label.pack(side='top')
    label = tkinter.Label(frame_label,
                          text='    Python第三方库在线安装程序  \n',
                          font=('simkai.ttf', 16))
    label.pack()
    # 第三方库是否安装选项

    # var变量
    vartext_numpy = tkinter.IntVar()
    vartext_matplotlib = tkinter.IntVar()
    # 建立frame
    numpy_matplotlib_frame = tkinter.Frame(frame)
    numpy_matplotlib_frame.pack(side='top')
    # 建立选项按钮
    numpy_checkbutton = tkinter.Checkbutton(
        numpy_matplotlib_frame,
        text='NumPy',
        variable=vartext_numpy,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_numpy, 'numpy'))
    numpy_checkbutton.pack(side='left')
    matplotlib_checkbutton = tkinter.Checkbutton(
        numpy_matplotlib_frame,
        text='Matplotlib',
        variable=vartext_matplotlib,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_matplotlib, 'matplotlib'))
    matplotlib_checkbutton.pack(side='right')

    # var变量
    vartext_pillow = tkinter.IntVar()
    vartext_sklearn = tkinter.IntVar()
    # 建立frame
    pillow_sklearn_frame = tkinter.Frame(frame)
    pillow_sklearn_frame.pack()
    # 建立选项按钮
    pillow_checkbutton = tkinter.Checkbutton(
        pillow_sklearn_frame,
        text='PIL',
        variable=vartext_pillow,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_pillow, 'pillow'))
    pillow_checkbutton.pack(side='left')
    matplotlib_checkbutton = tkinter.Checkbutton(
        pillow_sklearn_frame,
        text='Scikit-Learn',
        variable=vartext_sklearn,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_sklearn, 'sklearn'))
    matplotlib_checkbutton.pack(side='right')

    # var变量
    vartext_requests = tkinter.IntVar()
    vartext_bs4 = tkinter.IntVar()
    # 建立frame
    requests_bs4_frame = tkinter.Frame(frame)
    requests_bs4_frame.pack()
    # 建立选项按钮
    requests_checkbutton = tkinter.Checkbutton(
        requests_bs4_frame,
        text='Requests',
        variable=vartext_requests,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_requests, 'requests'))
    requests_checkbutton.pack(side='left')
    matplotlib_checkbutton = tkinter.Checkbutton(
        requests_bs4_frame,
        text='BeautifulSoup',
        variable=vartext_bs4,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_bs4, 'beautifulsoup4'))
    matplotlib_checkbutton.pack(side='right')

    # var变量
    vartext_jieba = tkinter.IntVar()
    vartext_wheel = tkinter.IntVar()
    # 建立frame
    jieba_wheel_frame = tkinter.Frame(frame)
    jieba_wheel_frame.pack()
    # 建立选项按钮
    jieba_checkbutton = tkinter.Checkbutton(
        jieba_wheel_frame,
        text='Jieba',
        variable=vartext_jieba,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_jieba, 'jieba'))
    jieba_checkbutton.pack(side='left')
    matplotlib_checkbutton = tkinter.Checkbutton(
        jieba_wheel_frame,
        text='Wheel',
        variable=vartext_wheel,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_wheel, 'wheel'))
    matplotlib_checkbutton.pack(side='right')

    # var变量
    vartext_pyinstaller = tkinter.IntVar()
    vartext_django = tkinter.IntVar()
    # 建立frame
    pyinstaller_django_frame = tkinter.Frame(frame)
    pyinstaller_django_frame.pack()
    # 建立选项按钮
    pyinstaller_checkbutton = tkinter.Checkbutton(
        pyinstaller_django_frame,
        text='PyInstaller',
        variable=vartext_pyinstaller,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_pyinstaller, 'pyinstaller'))
    pyinstaller_checkbutton.pack(side='left')
    matplotlib_checkbutton = tkinter.Checkbutton(
        pyinstaller_django_frame,
        text='Django',
        variable=vartext_django,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_django, 'django'))
    matplotlib_checkbutton.pack(side='right')

    # var变量
    vartext_flask = tkinter.IntVar()
    vartext_werobot = tkinter.IntVar()
    # 建立frame
    flask_werobot_frame = tkinter.Frame(frame)
    flask_werobot_frame.pack()
    # 建立选项按钮
    flask_checkbutton = tkinter.Checkbutton(
        flask_werobot_frame,
        text='Flask',
        variable=vartext_flask,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_flask, 'flask'))
    flask_checkbutton.pack(side='left')
    matplotlib_checkbutton = tkinter.Checkbutton(
        flask_werobot_frame,
        text='WeRoBot',
        variable=vartext_werobot,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_werobot, 'werobot'))
    matplotlib_checkbutton.pack(side='right')

    # var变量
    vartext_sympy = tkinter.IntVar()
    vartext_pandas = tkinter.IntVar()
    # 建立frame
    sympy_pandas_frame = tkinter.Frame(frame)
    sympy_pandas_frame.pack()
    # 建立选项按钮
    sympy_checkbutton = tkinter.Checkbutton(
        sympy_pandas_frame,
        text='SymPy',
        variable=vartext_sympy,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_sympy, 'sympy'))
    sympy_checkbutton.pack(side='left')
    matplotlib_checkbutton = tkinter.Checkbutton(
        sympy_pandas_frame,
        text='Pandas',
        variable=vartext_pandas,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_pandas, 'pandas'))
    matplotlib_checkbutton.pack(side='right')

    # var变量
    vartext_networkx = tkinter.IntVar()
    vartext_pyqt5 = tkinter.IntVar()
    # 建立frame
    networkx_pyqt5_frame = tkinter.Frame(frame)
    networkx_pyqt5_frame.pack()
    # 建立选项按钮
    networkx_checkbutton = tkinter.Checkbutton(
        networkx_pyqt5_frame,
        text='Networkx',
        variable=vartext_networkx,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_networkx, 'networks'))
    networkx_checkbutton.pack(side='left')
    matplotlib_checkbutton = tkinter.Checkbutton(
        networkx_pyqt5_frame,
        text='PyQt5',
        variable=vartext_pyqt5,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_pyqt5, 'pyqt5'))
    matplotlib_checkbutton.pack(side='right')

    # var变量
    vartext_pyopengl = tkinter.IntVar()
    vartext_pypdf2 = tkinter.IntVar()
    # 建立frame
    pyopengl_pypdf2_frame = tkinter.Frame(frame)
    pyopengl_pypdf2_frame.pack()
    # 建立选项按钮
    pyopengl_checkbutton = tkinter.Checkbutton(
        pyopengl_pypdf2_frame,
        text='PyOpenGL',
        variable=vartext_pyopengl,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_pyopengl, 'pyopengl'))
    pyopengl_checkbutton.pack(side='left')
    matplotlib_checkbutton = tkinter.Checkbutton(
        pyopengl_pypdf2_frame,
        text='PyPDF2',
        variable=vartext_pypdf2,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_pypdf2, 'pypdf2'))
    matplotlib_checkbutton.pack(side='right')

    # var变量
    vartext_docopt = tkinter.IntVar()
    vartext_pygame = tkinter.IntVar()
    # 建立frame
    docopt_pygame_frame = tkinter.Frame(frame)
    docopt_pygame_frame.pack()
    # 建立选项按钮
    docopt_checkbutton = tkinter.Checkbutton(
        docopt_pygame_frame,
        text='Docopt',
        variable=vartext_docopt,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_docopt, 'docopt'))
    docopt_checkbutton.pack(side='left')
    matplotlib_checkbutton = tkinter.Checkbutton(
        docopt_pygame_frame,
        text='PyGame',
        variable=vartext_pygame,
        onvalue=1,
        offvalue=0,
        command=lambda: select(vartext_pygame, 'pygame'))
    matplotlib_checkbutton.pack(side='right')

    # 安装按钮
    install_exit_frame = tkinter.Frame(frame)
    install_exit_frame.pack(side='bottom')

    install_button = tkinter.Button(install_exit_frame,
                                    text='安装',
                                    font=('simkai.ttf', 16),
                                    width=5,
                                    height=1,
                                    command=install)
    install_button.pack(side='left')
    exit_button = tkinter.Button(install_exit_frame,
                                 text='退出',
                                 font=('simkai.ttf', 16),
                                 width=5,
                                 height=1,
                                 command=window.quit)
    exit_button.pack(side='right')

    window.mainloop()


graphical()
