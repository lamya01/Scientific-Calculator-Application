from tkinter import *          #module for creating a graphic user interface
from functools import partial  #lets u deive a func with x parameters to a func with fewer parameters
#string that stores the instructions to be followed whike giving inputs
 
count=0
recall=[]
num=1
operationl=["+","-","*","/"]
row=0

back=0
front=0

main=Tk()                            #create the main calculator window
main.title("SCIENTIFIC CALCULTOR")   #to give a title to the window
main.geometry("500x590")             #provides dimentions to the window
main.configure(background="black")   #specifies the backgorund colour

def docalc(data):                       
    if(type(data)==int):
      entrybox.insert(END,str(data)) 
    else:
        entrybox.insert(END,data)

def find_exp(s):         #function to return expression in pyhton excecutable form eg:input sin(x) function returns math.sin(x)
    a=0
    '''s=entrybox.get()    #command to get the input from the entrybox'''
    b=len(s)
    while(a<b):
        if(s[a-1]!='.' and s[a-1]!='a' and s[a]=='s' and s[a+1]=='i' and s[a+2]=='n' and s[a+3]=='('):
          s=s[:a]+"math."+s[a:]
        elif(s[a-1]!='.' and s[a-1]!='a' and s[a]=='c' and s[a+1]=='o' and s[a+2]=='s' and s[a+3]=='('):
            s=s[:a]+"math."+s[a:]
        elif(s[a-1]!='.' and s[a-1]!='a' and s[a]=='t' and s[a+1]=='a' and s[a+2]=='n' and s[a+3]=="("):
            s=s[:a]+"math."+s[a:]
        elif(s[a-1]!='.' and s[a-1]!='a' and s[a]=='s' and s[a+1]=='e' and s[a+2]=='c' and s[a+3]=="("):
            s=s[:a]+"1/math.cos"+s[a+3:]
        elif(s[a-1]!='.' and s[a-1]!='a' and s[a]=='c' and s[a+1]=='o' and s[a+2]=='s' and s[a+3]=='e' and s[a+5]=="("):
            s=s[:a]+"1/math.sin"+s[a+5:]
        elif(s[a-1]!='.' and s[a-1]!='a' and s[a]=='c' and s[a+1]=='o' and s[a+2]=='t' and s[a+3]=="("):
            s=s[:a]+"1/math.tan"+s[a+3:]
        elif(s[a-1]!='.' and s[a]=='a' and s[a+1]=='s' and s[a+4]=='('):
            s=s[:a]+"math."+s[a:]
        elif(s[a-1]!='.' and s[a]=='a' and s[a+1]=='c' and s[a+4]=='('):
            s=s[:a]+"math."+s[a:]
        elif(s[a-1]!='.' and s[a]=='a' and s[a+1]=='t' and s[a+4]=='('):
            s=s[:a]+"math."+s[a:]
        elif(s[a-1]!='.' and s[a]=='a' and s[a+1]=='c' and s[a+4]=='e' and s[a+6]=='('):
            s=s[:a]+"1/math.asin"+s[a+6:]
        elif(s[a-1]!='.' and s[a]=='a' and s[a+1]=='s' and s[a+2]=='e' and s[a+4]=='('):
            s=s[:a]+"1.math.acos"+s[a+4:]
        elif(s[a-1]!='.' and s[a]=='a' and s[a+1]=='c' and s[a+2]=='o' and s[a+4]=='('):
            s=s[:a]+"1/math.atan"+s[a+4:]
        elif(s[a-1]!='.' and s[a-1]!='a' and s[a]=='s' and s[a+1]=='i' and s[a+2]=='n' and s[a+3]=='h' and s[a+4]=='('):
            s=s[:a]+"math."+s[a:]
        elif(s[a-1]!='.' and s[a-1]!='a' and s[a]=='c' and s[a+1]=='o' and s[a+2]=='s' and s[a+3]=='h' and s[a+4]=='('):
            s=s[:a]+"math."+s[a:]
        elif(s[a-1]!='.' and s[a-1]!='a' and s[a]=='t' and s[a+1]=='a' and s[a+2]=='n' and s[a+3]=='h' and s[a+4]=='('):
            s=s[:a]+"math."+s[a:]       
        b=len(s)      #updating the length of b everytime 
        a+=1
    print(s)
    return s

def cubic():
    s=entrybox.get()
    u=(-1+3j)/2
    l=s.split()
    for i in range(len(l)):
        l[i]=int(l[i])
    do=(l[1]**2)-(3*l[0]*l[2])
    d1=2*(l[1]**3)-(9*l[0]*l[1]*l[2])+27*(l[0]**2)*l[3]
    d=((d1**2)-4*(do**3))/(-1*27*(l[0]**2))
    c=(((((d1**2)-4*(do**3))+d1)**0.5)/2)**0.5
    r1=(l[1]+(u**1)*c+(do/(u**1)*c))/3*l[0]
    r2=(l[1]+(u**2)*c+(do/(u**2)*c))/3*l[0]
    r3=(l[1]+(u**3)*c+(do/(u**3)*c))/3*l[0]
    if(r1==r2 and r2==r3):
      output.configure(state="normal")
      output.insert(END,"equal roots")
      output.configure(state="disabled")
    else:
        output.configure(state="normal")
        output.insert(END,"unequal roots")
        output.configure(state="disabled")

def calculate():    # to calculate exp that is in python executible form
    import math
    try:
       s1=entrybox.get()
       s=find_exp(s1)
       result=eval(s)    #eval function ececutes a string as a python statement
       output.configure(state="normal")
       output.insert(END,str(result) +"\n")
       output.configure(state="disabled")    #output box is disabled is order to restrict modification of the result by the user 
       recall.append(s)
       recall.append(result)        #every result along with the exp is appended to recall to acess them in the future
       entrybox.delete(0,END)       #clears the entry box
    except SyntaxError:            #if a syntax error is found the message below is dialayed in the outbox
          output.configure(state="normal")
          output.insert(END,"this is not a valid input\n")
          output.configure(state="disabled")

def doubleintegration():
    def reset():  #function to clear the entrybox for the next input
      op.delete('1.0',END)
      m1.delete(0,END)
      m2.delete(0,END)
      m3.delete(0,END)
      m4.delete(0,END)
      m5.delete(0,END)
    def back():        #function to go back to the calculator window
        doubleintegration.destroy()   #destroys the new window created
    doubleintegration=Tk()
    doubleintegration.title("doubleintegration")
    doubleintegration.geometry("500x270")        
    f3=Frame(doubleintegration)
    f3.grid(row=1,column=0)
    f1=Frame(doubleintegration)
    f1.grid(row=0,column=0)
    l1=Label(f1,width=10,height=2,text="upperlimit x")
    l1.grid(row=0,column=0,sticky=W)
    l1=Label(f1,width=10,height=2,text="lowerlimit x")
    l1.grid(row=2,column=0,sticky=W)
    l1=Label(f1,width=10,height=2,text="int2")
    l1.grid(row=1,column=1,sticky=W)
    m1=Entry(f1,width=10,bg="light grey")
    m1.grid(row=0,column=1,sticky=W)
    m2=Entry(f1,width=10,bg="light grey")
    m2.grid(row=2,column=1,sticky=W)
    l1=Label(f1,width=10,height=2,text="upperlimit y")
    l1.grid(row=0,column=2,sticky=W)
    l1=Label(f1,width=10,height=2,text="lowerlimit y")
    l1.grid(row=2,column=2,sticky=W)
    l1=Label(f1,width=10,height=2,text="int1")
    l1.grid(row=1,column=3,sticky=W)
    m3=Entry(f1,width=10,bg="light grey")
    m3.grid(row=0,column=3,sticky=W)
    m4=Entry(f1,width=10,bg="light grey")
    m4.grid(row=2,column=3,sticky=W)
    l1=Label(f1,width=10,height=2,text="function")
    l1.grid(row=1,column=4,sticky=W)
    m5=Entry(f1,width=10,bg="light grey")
    m5.grid(row=1,column=5,sticky=W)
    l1=Label(f1,width=10,height=2,text="dy dx")
    l1.grid(row=1,column=6,sticky=W)
    op=Text(f3,width=45,height=5,wrap=WORD,bg="white")
    op.grid(row=0,column=0,sticky=W)
    op.configure(state="disabled")
    Button(f3,text="integrate",width=10,bg="white",fg="black",command=back).grid(row=4,column=0,sticky=W) 
    Button(f3,text="back",width=10,bg="white",fg="black",command=back).grid(row=5,column=0,sticky=W)
    Button(f3,text="reset",width=10,bg="white",fg="black",command=reset).grid(row=6,column=0,sticky=W) 

def integration():
  def reset():  #function to clear the entrybox for the next input
      op.delete('1.0',END)
      m1.delete(0,END)
      m2.delete(0,END)
      m3.delete(0,END)
  def back():        #function to go back to the calculator window
      integration.destroy()   #destroys the new window created
  def integral():
      area=0
      l1=[]
      import math
      s=m3.get()
      sn=find_exp(s)   #s stores the string returned form the find_exp() function
      a=int(m2.get())
      b=int(m1.get())
      l1.append(a)
      l1.append(b)
      n=abs(b-a)*10000    #n defines the number of rectangle or strips to be integrated over
      dx=0.0001           #dx is the small width of each rectangle
      mn=min(l1)
      for i in range(n):
          x=mn+i*dx
          ay=eval(sn)
          x=mn+(i+1)*dx
          by=eval(sn)
          area=area+0.5*(ay+by)*dx
      area=abs(area)    #incase the area is negative the abssolute value is taken
      op.configure(state="normal")
      op.insert(END,area)
      op.configure(state="disabled")
      recall.append(s)
      recall.append(area)
  integration=Tk()
  integration.title("integration")
  integration.geometry("350x270")
  f1=Frame(integration)
  f1.grid(row=0,column=0)
  f3=Frame(integration)
  f3.grid(row=1,column=0)
  l1=Label(f1,width=6,height=2,text="upperlimit")
  l1.grid(row=0,column=0,sticky=W)
  l2=Label(f1,width=6,height=2,text="lowerlimit")
  l2.grid(row=2,column=0,sticky=W)
  l3=Label(f1,width=6,height=2,text="function")
  l3.grid(row=1,column=1,sticky=W)
  l4=Label(f1,width=6,height=2,text="dx")
  l4.grid(row=1,column=3,sticky=W)
  m1=Entry(f1,width=10,bg="light grey")
  m1.grid(row=0,column=1,sticky=W)
  m2=Entry(f1,width=10,bg="light grey")
  m2.grid(row=2,column=1,sticky=W)
  m3=Entry(f1,width=10,bg="light grey")
  m3.grid(row=1,column=2,sticky=W)
  op=Text(f3,width=45,height=5,wrap=WORD,bg="white")
  op.grid(row=0,column=0,sticky=W)
  op.configure(state="disabled")
  Button(f3,text="integrate",width=10,bg="white",fg="black",command=integral).grid(row=4,column=0,sticky=W) 
  Button(f3,text="back",width=10,bg="white",fg="black",command=back).grid(row=5,column=0,sticky=W)
  Button(f3,text="reset",width=10,bg="white",fg="black",command=reset).grid(row=6,column=0,sticky=W) 
   
def leq():       #function to solve linear eq
    def reset():  #function to clear the entrybox for the next input
        output.configure(state="normal")
        output.delete("1.0",END)    #deletes the contents of the outbox
        output.configure(state="disabled")
        for i in range(len(l2)):      
            l2[i].delete(0,END)   #deletes the contents of the input box
        for j in range(len(l1)):      
            l1[j].delete(0,END)
    def back():        #function to go back to the calculator window
        linear.destroy()   #destroys the new window created
    def det(d,n):   #function to find out nxn determinant
      z=-1
      sum=0
      sum1=0
      sum2=0
      l1=[]
      if(n==2):  
        return d[0][0]*d[1][1]-d[0][1]*d[1][0]
      elif(n==1):
          return d[0][0]
      else:
          for k in range(n):
              for i in range(n):
                  if(i!=0):
                    l1.append([])
                  for j in range(n):
                      if(i!=0 and j!=k):
                        l1[i-1].append(d[i][j])
              sum1=((-1)**k)*d[0][k]*det(l1,n-1)
              sum=sum+sum1
              l1=[]
          sum2=sum
          sum=0
          return sum2
    def le():     #function to solve the linear eq
        l3=[]
        l4=[]
        d1=[]
        sol=[]
        c=-1
        l5=[]
        for i in range(len(l1)):
            if(i%int(s)==0):
              l3.append([])
            l3[c].append(int(l1[i].get()))
        for j in range(int(s)):
            l4.append(int(l2[j].get()))
            l5.append([])
        for h in range(int(s)):
            for g in range(int(s)):
                l5[h].append(0)
        print(l3,l4)
        print(l5)
        d=det(l3,int(s))
        print(d)
        for k in range(int(s)):
            for a in range(int(s)):
                for b in range(int(s)):
                    l5[a][b]=l3[a][b]
            for l in range(int(s)):
                l5[l][k]=l4[l]
            d1.append(det(l5,int(s)))
        print(d1)
        if(d!=0):
          for n in range(int(s)):
              output.configure(state="normal")
              output.insert(END,str(d1[n]/d)+" ")
              output.configure(state="disabled")
        d2=[]
        for l in range(len(d1)):
            d2.append(0)
        if(d2==d1):
          output.configure(state="normal")
          output.insert(END,"infinite number of solutions")
          output.configure(state="disabled")
        for ele in d1:
            if(ele!=0):
               if(d==0):
                 output.configure(state="normal")
                 output.insert(END,"no solution")
                 output.configure(state="disabled")
    l1=[]
    l2=[]
    s=entrybox.get()
    if(s.isdigit()):
      linear=Tk()
      linear.title("linear equation")
      if(int(s)<4):
        strr="370x250"     #till 4x4
      elif(int(s)==4):
          strr="370x275"
      else:
          n=int(s)-5
          x=385+65*n
          y=300+20*n
          strr=str(x)+"x"+str(y)
      linear.geometry(strr)
      linear.configure(background="black")
      f3=Frame(linear)
      f3.grid(row=0,column=0)
      f5=Frame(linear)
      f5.grid(row=2,column=0)
      l=Label(f3,width=6,height=2,text="cofficients")
      l.grid(row=0,column=0,sticky=W)
      l=Label(f3,width=6,height=2,text="constants")
      l.grid(row=0,column=int(s),sticky=W)    
      for i in range(int(s)):
          for j in range(int(s)):
              m1=Entry(f3,width=10,bg="light grey")
              m1.grid(row=i+1,column=j,sticky=W)
              l1.append(m1)
      for k in range(int(s)):
              m2=Entry(f3,width=10,bg="light grey")
              m2.grid(row=k+1,column=int(s),sticky=W)  
              l2.append(m2)
      output=Text(f5,width=45,height=5,wrap=WORD,bg="white")
      output.grid(row=0,column=0,sticky=W)
      output.configure(state="disabled")
      Button(f5,text="solve",width=10,bg="white",fg="black",command=le).grid(row=4,column=0,sticky=W) 
      Button(f5,text="back",width=10,bg="white",fg="black",command=back).grid(row=5,column=0,sticky=W)
      Button(f5,text="reset",width=10,bg="white",fg="black",command=reset).grid(row=6,column=0,sticky=W) 
    else:
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")          

def input_matrix():
  try:
    def reset():
        output.configure(state="normal")
        output.delete("1.0",END)
        output.configure(state="disabled")
        for i in range(len(l2)):      
            l2[i].delete(0,END)   
    def back():
        matrix.destroy()
    def det(d,n):
      z=-1
      sum=0
      sum1=0
      sum2=0
      l1=[]
      if(n==2):
        return d[0][0]*d[1][1]-d[0][1]*d[1][0]
      elif(len(d)==1):
          return d[0][0]
      else:
          for k in range(n):
              for i in range(n):
                  if(i!=0):
                    l1.append([])
                  for j in range(n):
                      if(i!=0 and j!=k):
                        l1[i-1].append(d[i][j])
              sum1=((-1)**k)*d[0][k]*det(l1,n-1)
              sum=sum+sum1
              l1=[]
          sum2=sum
          sum=0
          return sum2
    def call_det():
        l=[]
        tl=[]
        inv=[]
        z=-1
        a=0
        c=-1
        for y in range(len(l2)):
            if(y%int(s)==0):
              l.append([])
              z+=1
            l[z].append(int(l2[y].get()))
        dt=det(l,int(s))
        if(dt==0):
          output.configure(state="normal")
          output.insert(END,"inverse does not exist\n")
          output.configure(state="disabled")
        else:
         for i in range(len(l)):
             inv.append([])
             c+=1
             for j in range(len(l)):
                 z=-1
                 tl=[]
                 for k in range(len(l)):
                     if(k!=i):
                       tl.append([])
                       z+=1
                     for m in range(len(l)):
                         if(k!=i and m!=j):
                           tl[z].append(l[k][m])
                 inv[c].append(((-1)**a)*det(tl,z+1))
                 a+=1
         print(inv)
         invn=[]
         b=-1
         for i in range(len(inv)):
             invn.append([])
             b+=1 
             for j in range(len(inv)):
                 invn[b].append(inv[j][i]/dt) 
         for o in range(len(inv)):
             output.configure(state="normal")
             output.insert(END,str(invn[o])+"\n")
             output.configure(state="disabled")  
    l2=[]     
    s=entrybox.get()
    if(int(s)<=3):
      strr="370x225"
    elif(int(s)==4 or int(s)==5):
        if(int(s)==4):
          strr="370x250"
        else:
            strr="370x275"
    else:
        n=int(s)-6
        x=385+65*n
        y=280+20*n
        strr=str(x)+"x"+str(y)
    matrix=Tk()
    matrix.title("matrix multiplication")
    matrix.geometry(strr)
    matrix.configure(background="black")
    f3=Frame(matrix)
    f3.grid(row=0,column=0)
    f5=Frame(matrix)
    f5.grid(row=2,column=0)
    for i in range(int(s)):
          for j in range(int(s)):
              m1=Entry(f3,width=10,bg="light grey")
              m1.grid(row=i+1,column=j,sticky=W)
              l2.append(m1)
    output=Text(f5,width=45,height=5,wrap=WORD,bg="white")
    output.grid(row=0,column=0,sticky=W)
    output.configure(state="disabled")
    Button(f5,text="find_inverse",width=10,bg="white",fg="black",command=call_det).grid(row=4,column=0,sticky=W) 
    Button(f5,text="back",width=10,bg="white",fg="black",command=back).grid(row=5,column=0,sticky=W)
    Button(f5,text="reset",width=10,bg="white",fg="black",command=reset).grid(row=6,column=0,sticky=W)
  except(ZeroDivisionError):
      output.configure(state="normal")
      output.insert(END,"inverse does not exist")
      output.configure(state="disabled")           

def matrix_mul():
    def reset():
        output.configure(state="normal")
        output.delete("1.0",END)
        output.configure(state="disabled")
        for i in range(len(l2)):  
            l1[i].delete(0,END)    
            l2[i].delete(0,END)   
    def back():
        matrix.destroy()
    def multiply():
        l3=[]
        l4=[]
        l5=[]
        c=-1
        for i in range(len(l1)):
            if(i%int(s)==0):
               l3.append([])
               l4.append([])
               c+=1
            l3[c].append(int(l1[i].get()))
            l4[c].append(int(l2[i].get()))
        print(l3,l4)
        for w in range(len(l3)):
            l=[]
            for x in range(len(l3)):
                l.append(l3[w][x])
            for y in range(len(l3)):
                sum=0
                for z in range(len(l3)):
                    sum=sum+l[z]*l4[z][y]
                l5.append(sum)
        for o in range(len(l5)):
            if(o%int(s)==0):
              output.configure(state="normal")
              output.insert(END,"\n")
              output.configure(state="disabled")
            output.configure(state="normal")
            output.insert(END,str(l5[o])+" ")
            output.configure(state="disabled")            
    l1=[]
    l2=[]
    a=0
    s=entrybox.get()
    if(s.isdigit()):
      if(int(s)<=2):
        strr="366x250"
      else:
          n=int(s)-3
          x=386+129*n
          y=270+20*n
          strr=str(x)+"x"+str(y)
      matrix=Tk()
      matrix.title("matrix multiplication")
      matrix.geometry(strr)
      matrix.configure(background="black")
      f3=Frame(matrix)
      f3.grid(row=0,column=0)
      f5=Frame(matrix)
      f5.grid(row=2,column=0)
      l=Label(f3,width=6,height=2,text="matrix A")
      l.grid(row=0,column=0,sticky=W)
      l=Label(f3,width=6,height=2,text="matrix B")
      l.grid(row=0,column=int(s),sticky=W)    
      for i in range(int(s)):
          for j in range(int(s)):
              m1=Entry(f3,width=10,bg="light grey")
              m1.grid(row=i+1,column=j,sticky=W)
              l1.append(m1)
      for k in range(int(s)):
          for l in range(int(s)):
              m2=Entry(f3,width=10,bg="light grey")
              m2.grid(row=k+1,column=l+int(s),sticky=W)  
              l2.append(m2)
      output=Text(f5,width=45,height=5,wrap=WORD,bg="white")
      output.grid(row=0,column=0,sticky=W)
      output.configure(state="disabled")
      Button(f5,text="multiply",width=10,bg="white",fg="black",command=multiply).grid(row=4,column=0,sticky=W) 
      Button(f5,text="back",width=10,bg="white",fg="black",command=back).grid(row=5,column=0,sticky=W)
      Button(f5,text="reset",width=10,bg="white",fg="black",command=reset).grid(row=6,column=0,sticky=W) 
    else:
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")          
 
def input_det():
    def reset():
        output.configure(state="normal")
        output.delete("1.0",END)
        output.configure(state="disabled")
        for i in range(len(l2)):    
            l2[i].delete(0,END)

    def back():
        determinant.destroy()
    def det(d,n):
      z=-1
      if(d==[]):
        for y in range(len(l2)):
            if(y%n==0):
              d.append([])
              z+=1
            d[z].append(int(l2[y].get()))
        print(d)
        recall.append(d)
      sum=0
      sum1=0
      sum2=0
      l1=[]
      if(n==2):
        return d[0][0]*d[1][1]-d[0][1]*d[1][0]
      elif(n==1):
          return d[0][0]
      else:
          for k in range(n):
              for i in range(n):
                  if(i!=0):
                    l1.append([])
                  for j in range(n):
                      if(i!=0 and j!=k):
                        l1[i-1].append(d[i][j])
              print(d[0][k],l1,sep=" ")
              sum1=((-1)**k)*d[0][k]*det(l1,n-1)
              sum=sum+sum1
              l1=[]
          sum2=sum
          sum=0
          return sum2
    def call_det():
        l3=[]
        dt=det(l3,int(s))
        output.configure(state="normal")
        output.insert(END,str(dt)+"\n")
        output.configure(state="disabled")
        recall.append(dt)
    s=entrybox.get()
    l2=[]
    if(int(s)<=3):
      strr="370x225"
    elif(int(s)==4 or int(s)==5):
        if(int(s)==4):
          strr="370x250"
        else:
            strr="370x275"
    else:
        n=int(s)-6
        x=385+65*n
        y=280+20*n
        strr=str(x)+"x"+str(y)
    determinant=Tk()
    determinant.title("determinant")
    determinant.geometry(strr)
    determinant.configure(background="black")
    f3=Frame(determinant)
    f3.grid(row=0,column=0)
    f5=Frame(determinant)
    f5.grid(row=1,column=0)
    for i in range(int(s)):
          for j in range(int(s)):
              m1=Entry(f3,width=10,bg="light grey")
              m1.grid(row=i+1,column=j,sticky=W)
              l2.append(m1)
    output=Text(f5,width=45,height=5,wrap=WORD,bg="white")
    output.grid(row=0,column=0,sticky=W)
    output.configure(state="disabled")
    Button(f5,text="find_det",width=10,bg="white",fg="black",command=call_det).grid(row=4,column=0,sticky=W) 
    Button(f5,text="back",width=10,bg="white",fg="black",command=back).grid(row=5,column=0,sticky=W)
    Button(f5,text="reset",width=10,bg="white",fg="black",command=reset).grid(row=6,column=0,sticky=W)
    

def differentiation():
  def reset():
      op.delete("1.0",END)
      e1.delete(0,END)
      e2.delete(0,END)      
  def back():
      differentation.destroy()
  def differentiate():
      rd=0
      ld=0
      l=[]
      import math
      sn=e1.get()
      diff=find_exp(sn)   #gets expression in the python executable form
      i=0
      c=int(e2.get())
      dx=0.000000001  #infinitesimally small value
      x=c+dx
      y=eval(diff)
      rd=rd+y
      x=c
      y=eval(diff)
      rd=rd-y
      rd=rd/dx     #stores the right derivative
      ld=ld-y
      x=c-dx
      y=eval(diff)
      ld=ld+y
      ld=ld/-dx    #stores the left derivative
      op.configure(state="normal")
      op.insert(END,str(rd)+" "+str(ld)+"\n")
      op.configure(state="disabled")
      if(round(ld)==round(rd)):
        op.configure(state="normal")
        op.insert(END,"derivative is "+str(rd))
        op.configure(state="disabled")
        recall.append(sn)
        recall.append(rd)
      else:
          op.configure(state="normal")
          op.insert(END,"derivative does not exist")
          op.configure(state="disabled")
  differentation=Tk()
  differentation.title("differentation")
  differentation.geometry("420x250")
  f1=Frame(differentation)
  f1.grid(row=0,column=0)
  f2=Frame(differentation)
  f2.grid(row=1,column=0)
  l1=Label(f1,width=6,height=2,text="function")
  l1.grid(row=0,column=0,sticky=W)    
  l2=Label(f1,width=6,height=2,text="value")
  l2.grid(row=1,column=0,sticky=W)    
  e1=Entry(f1,width=60,bg="light grey")
  e1.grid(row=0,column=1,sticky=W)
  e2=Entry(f1,width=10,bg="light grey")
  e2.grid(row=1,column=1,sticky=W)
  op=Text(f2,width=45,height=5,wrap=WORD,bg="white")
  op.grid(row=0,column=0,sticky=W)
  op.configure(state="disabled")
  Button(f2,text="differentiate",width=10,bg="white",fg="black",command=differentiate).grid(row=1,column=0,sticky=W) 
  Button(f2,text="back",width=10,bg="white",fg="black",command=back).grid(row=2,column=0,sticky=W)
  Button(f2,text="reset",width=10,bg="white",fg="black",command=reset).grid(row=3,column=0,sticky=W)

def p():
  try:
    pro=1
    s=entrybox.get()
    m=int(s[0])
    n=int(s[2])   # stores m and n form obtained from equation McN
    for i in range(m):
        pro=pro*(i+1)    #calculates m factorial
    for j in range(m-n):
        pro=pro/(j+1)    #calculates m-n factorial
    output.configure(state="normal")
    output.insert(END,str(pro))
    output.configure(state="disabled")
    recall.append(s)
    recall.append(pro)
  except (IndexError,ValueError):
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")

def c():
  try:
    pro=1
    s=entrybox.get()
    s=s.split(" ")
    m=int(s[0])
    n=int(s[1])
    for i in range(m):
        pro=pro*(i+1)   #calculates m factorial
    for j in range(n):
        pro=pro/(j+1)   #calculates n factorial
    for k in range(m-n):
        pro=pro/(k+1)   #calculates m-n factorial
    output.configure(state="normal")
    output.insert(END,str(pro))
    output.configure(state="disabled")
    recall.append(s)
    recall.append(pro)
  except (IndexError,ValueError):
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")

def summation():
  try:
    import math
    s=find_exp()
    l=s.split(" ")
    sm=l[0]       #stores the function to be summated over
    a=int(l[1])   #stores the lower limit of the range
    b=int(l[2])   #stores the upper limit of the range
    sum=0
    for i in range(a,b+1):
        x=i
        sum=sum+eval(sm)
    output.configure(state="normal")
    output.insert(END,str(sum))
    output.configure(state="disabled")
    recall.append(s)
    recall.append(sum)
  except IndexError:
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")

def bin_no():    #function to convert from binary to decimal
  c=0
  try:
    s=entrybox.get()
    l=s.split()
    for ele in s:
        if(ele not in ['0','1']):
          c=c+1                   #condition to check whether the input is valid or not
    if(c==0):       #if c=0 input is either 0 or 1 which is correct
      sum=0
      j=0
      for i in range((len(s)-1),-1,-1):
          if(s[j]=='1'):
            sum=sum+(2**i)     #2 to the power index of only the 1's gives the equivalent decimal number 
          j+=1
    
      recall.append(s)
      recall.append(sum)
      output.configure(state="normal")
      output.insert(END,str(sum)+"\n")       
      output.configure(state="disabled")
    else:
        output.configure(state="normal")
        output.insert(END,"invalid input")       
        output.configure(state="disabled")
  except IndexError:
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")

def proportion():    #function to find out x in expression x:a::b:c
  try:
    s=entrybox.get()     #entrybox function only returns a string
    l=s.split()
    for i in range(len(l)):
        if(l[0]=='x'):          #if ,elif conditions to check the position of x
          y=(int(l[2])/int(l[3]))*(int(l[1]))
        elif(l[1]=='x'):
            y=(int(l[0])*int(l[3]))/int(l[2])
        elif(l[2]=='x'):
            y=(int(l[0])*int(l[3]))/int(l[1])
        else:
            y=(int(l[1])*int(l[2]))/int(l[0])
    output.configure(state="normal")
    output.insert(END,str(y)+"\n")
    output.configure(state="disabled")
    recall.append(s)
    recall.append(y) 
  except (IndexError,ValueError):
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")    #anything that is printed in the output box must be a string
        output.configure(state="disabled")
                 
def clear():
    output.configure(state="normal")
    output.delete("1.0",END)          #command to delete the contents in the output box
    output.configure(state="disabled")  
    entrybox.delete(0,END)            #command to delete the contents of the entrybox
def quit():          #to exit from the calculator
    global main      #main is a name outside the function
    main.quit()      #to exit from the main

def rec():           #function to display the previous results
    global count     
    global recall    #global list that stores the operation and the result
    if(len(recall)==0):     #if length of recall is 0 then nothing is performed 
      output.configure(state="normal")
      output.insert(END,"no operation performed")
      output.configure(state="disabled")
    else:
        output.configure(state="normal")
        output.delete("1.0",END)         #command to delete the output contents
        output.configure(state="disabled")
        if((len(recall)-count)>=0):
          output.configure(state="normal")
          output.insert(END,recall[len(recall)-(count+2)])
          output.insert(END,"\n")
          output.insert(END,recall[len(recall)-(count+1)])
          output.configure(state="disabled")
        count+=2   
 
def fact():
  try:
    pro=1
    s=entrybox.get()
    s=int(s)
    for i in range(s):     #find the factorial of int(s)
        pro=pro*(i+1)
    s=str(s)+'!'
    output.configure(state="normal")
    output.insert(END,str(pro))
    output.configure(state="disabled")
    recall.append(s)
    recall.append(str(pro))
  except (IndexError,ValueError):
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")
       
def space():
    entrybox.insert(END," ")      #function to insert into the entrybox

def get_info():                   #function that returns the current postion of the cursor
    return entrybox.index(INSERT)

def left():                       #function to move the cursor on step left
    entrybox.icursor(get_info()-1)

def right():                      #function to move the cursor on step right
    s=entrybox.get()              #in order to move one step right we need to know the current position
    if(get_info()<(len(s)-1)):
      entrybox.icursor(get_info()+1)
    elif(get_info()==(len(s)-1)):
        entrybox.icursor(END)

def complex():    #generates the euler form of a complex number
  try:
    string=""
    s=entrybox.get()     #takes 2 number as parameters as a string
    l=s.split()
    l[0]=int(l[0])       #1st number
    l[1]=int(l[1])       #2nd number
    import math
    angle=math.atan(l[1]/l[0])    #angle formula:atan(b/a)
    dis=math.sqrt((l[0]**2)+(l[1]**2))      #distance from origin formula:sqrt(a**2+b**2)
    string=string+str(dis)+"*e^(i"+str(angle)+")"
    recall.append(s)
    recall.append(string)
    output.configure(state="normal")
    output.insert(END,string)
    output.configure(state="disabled")
    recall.append(s)
    recall.append(string)
  except (IndexError,ValueError):
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")

def inequality():    #solves quadratic inequality
  try:
    s=entrybox.get()  #takes 3 numbers and a inequality symbol in the form of a string
    st=""
    l=s.split(" ")
    a=int(l[0])    #1st number
    b=int(l[1])    #2nd number
    c=int(l[2])    #3rd number
    d1=(-b+(((b**2)-4*a*c)**0.5))/2*a     #root1
    d2=(-b-(((b**2)-4*a*c)**0.5))/2*a     #root2
    if(l[len(l)-1]=='>'):   #if and elif condition decide the interval of solution based on the inequality symbol entered
      st=st+"(-inf,"+str(d2)+") U ("+str(d1)+",+inf)"
    elif(l[len(l)-1]=='<'):
        st=st+"("+str(d2)+","+str(d1)+")"
    elif(l[len(l)-1]=='<='):
        st=st+"["+str(d2)+","+str(d1)+"]"
    elif(l[len(l)-1]=='>='):
        st=st+"(-inf,"+str(d2)+"] U ["+str(d1)+",+inf)"
    output.configure(state="normal")
    output.insert(END,st)
    output.configure(state="disabled")
    recall.append(l[0]+"x**2+"+l[1]+"x+"+l[2]+l[3]+"0")
    recall.append(st)
  except (IndexError,ValueError):
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")

def hxdec():
  try:
    str1=[]
    s=entrybox.get()    
    q=int(s)
    if(q==0):
      output.configure(state="normal")
      output.insert(END,"0")
      output.configure(state="disabled")
    hex={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    while(q!=0):     
         r=q%16
         str1.append(hex[r])
         q=q//16
    str1.reverse()
    str2="".join(str(e) for e in str1)    
    output.configure(state="normal")
    output.insert(END,str2)
    output.configure(state="disabled")
    recall.append(s)
    recall.append(str2)
  except (IndexError,ValueError):
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")

def dec_oct():
    try:
       l=[]
       s=entrybox.get()
       num=int(s)
       while(num!=0):
            r=num%8
            num=num//8
            l.append(r)
       l.reverse()
       str2="".join(str(e) for e in l)
       output.configure(state="normal")
       output.insert(END,str2)
       output.configure(state="disabled")
       recall.append(s)
       recall.append(str2)
    except (IndexError,ValueError):
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")

def oct_dec():
  try:
     s=entrybox.get()
     l=[]
     for ele in s:
         l.append(int(ele))
     l.reverse()
     sum=0
     for i in range(len(l)):
         sum=sum+l[i]*(8**i)
     output.configure(state="normal")
     output.insert(END,str(sum))
     output.configure(state="disabled")
     recall.append(s)
     recall.append(str(sum))
  except (IndexError,ValueError):
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")  

def hxnum():
    try:
       sum=0
       hex={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
       s=entrybox.get()
       l=[]
       for ele in s:
           l.append(ele)
       l.reverse()
       for i in range(len(l)):
           sum=sum+hex[l[i]]*(16**i)
       output.configure(state="normal")
       output.insert(END,str(sum))
       output.configure(state="disabled")
       recall.append(s)
       recall.append(str(sum))
    except (IndexError,ValueError):
        output.configure(state="normal")
        output.insert(END,"this is not a valid input\n")
        output.configure(state="disabled")        

def hlp():           # function to display the input instructions
    def clr():
        op.configure(state="normal")
        op.delete("1.0",END)          
        op.configure(state="disabled")  
        en.delete(0,END)            
    def search():
        fin =open("instructions.txt",'r')
        txt=fin.read()
        l=txt.split("\n")
        s=en.get()
        for ele in l:
            l1=ele.split(" ")
            if(l1[0]==s):
              op.configure(state="normal")
              op.insert(END,ele)      #inserts the help_str string which contains all the input instructions
              op.configure(state="disabled")
    window1=Tk()     #creates a new window named window1
    window1.title("HELP")
    window1.geometry("405x210")
    window1.configure(background="black")
    f1=Frame(window1)
    f1.grid(row=0,column=0)
    f2=Frame(window1)
    f2.grid(row=1,column=0)
    f3=Frame(window1)
    f3.grid(row=2,column=0)
    def back():       #funtion to go back to the calculated window
        window1.destroy()
    en=Entry(f1,width=60,bg="light grey")
    en.grid(row=0,column=0,sticky=W)
    op=Text(f2,width=50,height=10,wrap=WORD,bg="white")   #creates a output text box
    op.grid(row=1,column=0,sticky=W)
    op.configure(state="disabled")
    
    Button(f3,text="back",width=10,bg="blue",fg="white",command=back).grid(row=0,column=0)
    Button(f3,text="search",width=10,bg="blue",fg="white",command=search).grid(row=0,column=1)
    Button(f3,text="clear",width=10,bg="blue",fg="white",command=clr).grid(row=0,column=2)

def clear1():        #function for back space
    output.configure(state="normal")
    output.delete("1.0",END)
    output.configure(state="disabled")
    n=int(len(entrybox.get()))
    print(n)    
    entrybox.delete(n-1,END)     #command to delete by one charecter  ie it deletes form n-1th charecter till nth charecter,which deletes the last charecter 

r1=1          #variables defines to specify the column number
r2=1
r3=1
r4=1
r5=1
r6=1
r7=1
r8=1
r9=1
r10=1
r11=1
    
numpad=Frame(bd=5)      #creates a frame named numpad
numpad.grid(row=1,column=0,sticky=W)
numpad.configure(background="black")

operations=Frame()       #frame created for the operation buttons
operations.grid(row=4,column=0)
f1=Frame()
f1.grid(row=5,column=0)
f2=Frame()
f2.grid(row=0,column=0)
f3=Frame()
f3.grid(row=5,column=1)
entrybox=Entry(f2,width=60,bg="light grey")
entrybox.grid(row=0,column=0,sticky=W)
output=Text(f2,width=45,height=5,wrap=WORD,bg="white")
output.grid(row=1,column=0,sticky=W)
output.configure(state="disabled")

for row in range(1,4):
    for column in range(3):
        if(num%2==0):
          Button(numpad,text=num,width=22,bg="red",fg="white",command=partial(docalc,num)).grid(row=row,column=column,sticky=W)
        else:
            Button(numpad,text=num,width=22,bg="black",fg="white",command=partial(docalc,num)).grid(row=row,column=column,sticky=W)
        num+=1
for i in operationl:
    if(i=='-' or i=='*'):
      Button(operations,text=i,width=15,bg="orange",fg="white",command=partial(docalc,i)).grid(row=4,column=row,sticky=W)
    else:
        Button(operations,text=i,width=15,bg="blue",fg="white",command=partial(docalc,i)).grid(row=4,column=row,sticky=W)
    row+=1

Button(f1,text="oct_dec",width=10,bg="black",fg="white",command=oct_dec).grid(row=8,column=r9,sticky=W);r9+=1
Button(f1,text="dec_oct",width=10,bg="black",fg="white",command=dec_oct).grid(row=8,column=r9,sticky=W);r9+=1
Button(f1,text="hex_num",width=10,bg="black",fg="white",command=hxnum).grid(row=8,column=r9,sticky=W);r9+=1
Button(f1,text="dec_hex",width=10,bg="black",fg="white",command=hxdec).grid(row=8,column=r9,sticky=W);r9+=1
Button(f1,text=">=<",width=10,bg="black",fg="white",command=inequality).grid(row=8,column=r9,sticky=W);r9+=1
Button(f1,text="help",width=10,bg="black",fg="white",command=hlp).grid(row=8,column=r9,sticky=W)

Button(f1,text="space",width=10,bg="black",fg="white",command=space).grid(row=7,column=r8,sticky=W);r8+=1
Button(f1,text="pi",width=10,bg="black",fg="white",command=partial(docalc,"math.pi")).grid(row=7,column=r8,sticky=W);r8+=1
Button(f1,text=">>",width=10,bg="black",fg="white",command=right).grid(row=7,column=r8,sticky=W);r8+=1
Button(f1,text="<<",width=10,bg="black",fg="white",command=left).grid(row=7,column=r8,sticky=W);r8+=1
Button(f1,text="10^x",width=10,bg="black",fg="white",command=partial(docalc,"10**")).grid(row=7,column=r8,sticky=W);r8+=1
Button(f1,text="euler",width=10,bg="black",fg="white",command=complex).grid(row=7,column=r8,sticky=W)

Button(numpad,text="off",width=10,bg="blue",fg="white",command=quit).grid(row=0,column=0)
Button(numpad,text="clear",width=10,bg="green",fg="white",command=clear).grid(row=0,column=1)
Button(numpad,text="recall",width=10,bg="blue",fg="white",command=rec).grid(row=0,column=2)
Button(f1,text="ratio",width=10,bg="black",fg="white",command=summation).grid(row=6,column=r7);r7+=1
Button(f1,text="x!",width=10,bg="black",fg="white",command=fact).grid(row=6,column=r7);r7+=1
Button(f1,text="^",width=10,bg="black",fg="white",command=partial(docalc,"^")).grid(row=6,column=r7);r7+=1
Button(f1,text="e",width=10,bg="black",fg="white",command=partial(docalc,"2.71828")).grid(row=6,column=r7);r7+=1
Button(f1,text="|x|",width=10,bg="black",fg="white",command=input_det).grid(row=6,column=r7,sticky=W);r7+=1
Button(f1,text="logx",width=10,bg="black",fg="white",command=partial(docalc,'math.log(')).grid(row=6,column=r7,sticky=W)

Button(numpad,text="=",width=22,bg="red",fg="white",command=calculate).grid(row=4,column=0,sticky=W)
Button(numpad,text="0",width=22,bg="black",fg="white",command=partial(docalc,"0")).grid(row=4,column=1)
Button(numpad,text=".",width=22,bg="red",fg="white",command=partial(docalc,".")).grid(row=4,column=2)

Button(f1,text="integration",width=10,bg="black",fg="white",command=integration).grid(row=2,column=r3,sticky=W);r3+=1
Button(f1,text="nPr",width=10,bg="black",fg="white",command=p).grid(row=2,column=r3,sticky=W);r3+=1
Button(f1,text="nCr",width=10,bg="black",fg="white",command=c).grid(row=2,column=r3,sticky=W);r3+=1
Button(f1,text="bin",width=10,bg="black",fg="white",command=partial(docalc,"bin")).grid(row=2,column=r3,sticky=W);r3+=1
Button(f1,text="bin_no",width=10,bg="black",fg="white",command=bin_no).grid(row=2,column=r3,sticky=W);r3+=1
Button(f1,text="differentiate",width=10,bg="black",fg="white",command=differentiation).grid(row=2,column=r3,sticky=W)

Button(f1,text="sum",width=10,bg="black",fg="white",command=proportion).grid(row=3,column=r4,sticky=W);r4+=1
Button(f1,text="y",width=10,bg="black",fg="white",command=partial(docalc,"y")).grid(row=3,column=r4,sticky=W);r4+=1
Button(f1,text="(",width=10,bg="black",fg="white",command=partial(docalc,"(")).grid(row=3,column=r4,sticky=W);r4+=1
Button(f1,text=")",width=10,bg="black",fg="white",command=partial(docalc,")")).grid(row=3,column=r4,sticky=W);r4+=1
Button(f1,text="x",width=10,bg="black",fg="white",command=partial(docalc,"x")).grid(row=3,column=r4,sticky=W);r4+=1
Button(f1,text="leq",width=10,bg="black",fg="white",command=leq).grid(row=3,column=r4,sticky=W)

Button(f1,text="sin",width=10,bg="black",fg="white",command=partial(docalc,"sin(")).grid(row=0,column=r1,sticky=W);r1+=1
Button(f1,text="cos",width=10,bg="black",fg="white",command=partial(docalc,"cos(")).grid(row=0,column=r1,sticky=W);r1+=1
Button(f1,text="tan",width=10,bg="black",fg="white",command=partial(docalc,"tan(")).grid(row=0,column=r1,sticky=W);r1+=1
Button(f1,text="cot",width=10,bg="black",fg="white",command=partial(docalc,"1/tan(")).grid(row=0,column=r1,sticky=W);r1+=1
Button(f1,text="sec",width=10,bg="black",fg="white",command=partial(docalc,"1/cos(")).grid(row=0,column=r1,sticky=W);r1+=1
Button(f1,text="cosec",widt=10,bg="black",fg="white",command=partial(docalc,"1/sin(")).grid(row=0,column=r1,sticky=W)
Button(f1,text="asin",width=10,bg="black",fg="white",command=partial(docalc,"asin(")).grid(row=1,column=r2,sticky=W);r2+=1
Button(f1,text="acos",width=10,bg="black",fg="white",command=partial(docalc,"acos(")).grid(row=1,column=r2,sticky=W);r2+=1
Button(f1,text="acot",width=10,bg="black",fg="white",command=partial(docalc,"1/atan(")).grid(row=1,column=r2,sticky=W);r2+=1
Button(f1,text="atan",width=10,bg="black",fg="white",command=partial(docalc,"atan(")).grid(row=1,column=r2,sticky=W);r2+=1
Button(f1,text="acosec",width=10,bg="black",fg="white",command=partial(docalc,"1/asin(")).grid(row=1,column=r2,sticky=W);r2+=1
Button(f1,text="asec",width=10,bg="black",fg="white",command=partial(docalc,"1/acos(")).grid(row=1,column=r2,sticky=W)

Button(f1,text="x^2",width=10,bg="black",fg="white",command=partial(docalc,"**2")).grid(row=4,column=r5);r5+=1
Button(f1,text="x^y",width=10,bg="black",fg="white",command=partial(docalc,"**")).grid(row=4,column=r5);r5+=1
Button(f1,text="x^-1",width=10,bg="black",fg="white",command=partial(docalc,"**-1")).grid(row=4,column=r5);r5+=1
Button(f1,text="x^0.5",width=10,bg="black",fg="white",command=partial(docalc,"**0.5")).grid(row=4,column=r5);r5+=1
Button(f1,text="x^(1/y)",width=10,bg="black",fg="white",command=partial(docalc,"**(1/")).grid(row=4,column=r5);r5+=1
Button(f1,text="abs",width=10,bg="black",fg="white",command=partial(docalc,"abs(")).grid(row=4,column=r5)

Button(f1,text="sinh",width=10,bg="black",fg="white",command=partial(docalc,"math.sinh(")).grid(row=5,column=r6);r6+=1
Button(f1,text="cosh",width=10,bg="black",fg="white",command=partial(docalc,"math.cosh(")).grid(row=5,column=r6);r6+=1
Button(f1,text="tanh",width=10,bg="black",fg="white",command=partial(docalc,"math.tanh(")).grid(row=5,column=r6);r6+=1
Button(f1,text="asinh",width=10,bg="black",fg="white",command=partial(docalc,"math.asinh(")).grid(row=5,column=r6);r6+=1
Button(f1,text="acosh",width=10,bg="black",fg="white",command=partial(docalc,"math.acosh(")).grid(row=5,column=r6);r6+=1
Button(f1,text="atanh",width=10,bg="black",fg="white",command=partial(docalc,"math.atanh(")).grid(row=5,column=r6)
Button(f1,text="matrix*",width=10,bg="black",fg="white",command=matrix_mul).grid(row=9,column=r10);r10+=1
Button(f1,text="matrix_inv",width=10,bg="black",fg="white",command=input_matrix).grid(row=9,column=r10);r10+=1
Button(f1,text="fx/gx",width=10,bg="black",fg="white",command=partial(docalc,"(()/())")).grid(row=9,column=r10);r10+=1
Button(f1,text="<---",width=10,bg="black",fg="white",command=clear1).grid(row=9,column=r10);r10+=1
Button(f1,text=",",width=10,bg="black",fg="white",command=partial(docalc,",")).grid(row=9,column=r10);r10+=1
Button(f1,text="cube_eq",width=10,bg="black",fg="white",command=cubic).grid(row=9,column=r10)
Button(f1,text="doubleint",width=10,bg="black",fg="white",command=doubleintegration).grid(row=10,column=r11)
 
main.mainloop()