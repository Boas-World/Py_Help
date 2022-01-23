class tk_short:
  def __init__():
    try:
      from tkinter import*
    except:
      pass
    print("Tk short version: 1.0.2")
  def Cube (C,x,y,L):
    C.create_rectangle(x,y,x+L,y+L)
  def Rect (C,x,y,L,l):
    C.create_rectangle(x,y,x+L,y+l)
  def Circle (C,x,y,R):
    C.create_oval(x,y,x+R,y+R)
  def Oval (C,x,y,L,l):
    C.create_oval(x,y,x+L,y+l)
  
