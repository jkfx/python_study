from tkinter import *

w = Tk()
w.geometry('500x300')
w.title('pack study')

Label(w, text='p', fg='red').pack(side='top')
Label(w, text='p', fg='red').pack(side='bottom')
Label(w, text='p', fg='red').pack(side='left')
Label(w, text='p', fg='red').pack(side='right')

w.mainloop()
