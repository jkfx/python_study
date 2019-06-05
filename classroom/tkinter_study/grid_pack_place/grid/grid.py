from tkinter import *

w = Tk()
w.geometry('500x300')
w.title('grid study')

for i in range(3):
    for j in range(3):
        Label(w, text=1).grid(row=i, column=j, padx=5, pady=5, ipadx=5, ipady=5)

w.mainloop()
