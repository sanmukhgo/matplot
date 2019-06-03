import tkinter as tk
import numpy as np
import matplotlib
from matplotlib.axes import Axes
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk #NavigationToolbar2Tk
from matplotlib.figure import Figure

def line(t,c=0):
    return t+c

def getinput():
    input = self.myText_Box.get("1.0",END)


def update():
    c=int(box.get())
    l.cla()
    setaxes(c)
    l.plot(t,line(t,c))
    canvas.draw()

def setaxes(c):
    Axes.set_ylim(l,bottom=c-5,top=c+10)

c=0
t=np.arange(0,10,0.02)

f=Figure(figsize=(10,5),dpi=100)
l=f.add_subplot(111)
setaxes(c)
l.plot(t,line(t,c))

root=tk.Tk()
root.title("Line Plot")

frame1=tk.Frame(root)
frame2=tk.Frame(root)
frame1.pack(side=tk.LEFT)
frame2.pack(side=tk.LEFT)

txt=tk.Label(frame1,text="c=")
txt.pack(side=tk.LEFT)

box=tk.Entry(frame1)
box.insert(0,"0")
box.pack(side=tk.LEFT)

b=tk.Button(frame1,text="Update",command=update)
b.pack(side=tk.BOTTOM)

canvas=FigureCanvasTkAgg(f,master=frame2)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=1)

toolbar=NavigationToolbar2Tk(canvas,frame2)
toolbar.update()
canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

root.mainloop()