from tkinter import *

w = Tk()
w.geometry('500x300')
w.title('Frame study')

Label(w, text='on the window', bg='red', font=('Arial', 16)).pack()

frame = Frame(w)
frame.pack()

frame_l = Frame(frame)
frame_r = Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')

Label(frame_l, text='on the frame_l1', bg='green').pack()
Label(frame_l, text='on the frame_l2', bg='green').pack()
Label(frame_l, text='on the frame_l3', bg='green').pack()
Label(frame_r, text='on the frame_r1', bg='yellow').pack()
Label(frame_r, text='on the frame_r2', bg='yellow').pack()
Label(frame_r, text='on the frame_r3', bg='yellow').pack()

w.mainloop()
