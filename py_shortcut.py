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
   def disk(x,y,Pd,Pf):
    for i in range(Pd,Pf):
      circle(i)

class SString(str):
  def __init__(self, S):
    self.S=S
  def int(self, **karg):
    try:
      return int(self.S[karg["start"]:karg["end"]])
    except:
      try:
        return int(self.S[0:karg["end"]])
      except:
        try:
          return int(self.S[karg["start"]:len(self.S)])
        except:
          try:
            return int(self.S)
          except :
            raise Exception("The strinbg isn't an int")
  def float(self, **karg):
    try:
      return float(self.S[karg["start"]:karg["end"]])
    except:
      try:
        return float(self.S[0:karg["end"]])
      except:
        try:
          return float(self.S[karg["start"]:len(self.S)])
        except:
          try:
            return float(self.S)
          except :
            raise Exception("The strinbg isn't an float")
  def Exception(self, **karg):
    try:
      return Exception(self.S[karg["start"]:karg["end"]])
    except:
      try:
        return Exception(self.S[0:karg["end"]])
      except:
        try:
          return Exception(self.S[karg["start"]:len(self.S)])
        except:
          try:
            return Exception(self.S)
          except :
            raise Exception("The strinbg isn't an float")
