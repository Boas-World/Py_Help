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

    
    
class Turtle_short:
  def __init__(self):
    try:
      from turtle import*
     except:
      pass
   def forigth(slef,A,a):
    for i in range(0,A):
      forward(1)
      right(a/A)
   def forleft(slef,A,a):
    for i in range(0,A):
      forward(1)
      left(a/A)
   def backrigth(slef,A,a):
    for i in range(0,A):
      backward(1)
      right(a/A)
   def backleft(slef,A,a):
    for i in range(0,A):
      backward(1)
      left(a/A)
      
      
