from tkinter import *
w = Tk()
w.geometry("690x496")
w.title("geek fx")
w.resizable(width=False, height=False)
Label(
    w,
    font=("C:/Windows/Fonts/fira code", 20),
    text="Hello world!",
    bg="black",
    fg="white",
).pack(side=TOP)
Button(w, text="登录", width=16, height=2).pack(side=BOTTOM)
Button(w, text="注册", width=16, height=2).pack(side=BOTTOM)
w.mainloop()
