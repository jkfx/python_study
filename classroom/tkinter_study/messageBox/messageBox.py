from tkinter import *
import tkinter.messagebox

w = Tk()
w.title('messageBox study')
w.geometry('500x300')

def hit_me():
    #tkinter.messagebox.showinfo(title='Hi', message='你好!')  # 提示信息对话窗
    #tkinter.messagebox.showwarning(title='Hi', message='有警告!')   # 提示警告对话窗
    tkinter.messagebox.showerror(title='Hi', message='出错了!')
    #tkinter.messagebox.askquestion(title='Hi', message='你好!')    # 提示选择对话框，return 'yes'/'no'
    #tkinter.messagebox.askyesno(title='Hi', message='你好!')    # return True/False
    #tkinter.messagebox.askokcancel(title='Hi', message='你好!')


Button(w, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()

w.mainloop()
