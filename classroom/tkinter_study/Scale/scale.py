from tkinter import *

w = Tk()
w.title('Scale')
w.geometry('500x300')

# 在图形界面上创建一个标签label用以显示并放置
l = Label(w, bg='green', fg='white', width=20, text='empty')
l.pack()


# 定义一个触发函数功能
def print_selection(v):
    l.config(text='you have selected ' + v)


# 创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为0.1，触发调用print_selection函数
s = Scale(w,
          #label='try me',
          from_=0,
          to=10,
          orient=HORIZONTAL,
          length=200,
          showvalue=2,
          resolution=0.1,
          command=print_selection)
s.pack()
w.mainloop()