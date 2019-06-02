from tkinter import *

w = Tk()
w.title('Canvas study')
w.geometry('500x300')

# 创建一个矩形，指定画布的颜色为白色
cv = Canvas(w, bg='white')
# arc − 创建一个扇形
coord = (10, 50, 240, 210)
cv.create_arc(coord, start=0, extent=150, fill='blue')
# line − 创建线条
cv.create_line(coord)
# oval − 创建一个圆
cv.create_oval(coord)
# polygon − 创建一个至少有三个顶点的多边形
cv.create_polygon(coord)
# rectangle - 创建一个矩形
cv.create_rectangle(coord)
cv.pack()
w.mainloop()
