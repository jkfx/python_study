from tkinter import *

w = Tk()
w.title('My Tkinter study')
w.geometry('500x300')

# 在图形界面上设定输入框控件entry并放置控件
e1 = Entry(w, show=None, font=('Arial', 14), cursor='circle')  # 显示成名文形式
e2 = Entry(w, show='*', font=('Arial', 14), cursor='cross')  # 显示成密文形式
e1.pack()
e2.pack()

w.mainloop()
