from selenium import webdriver
import tkinter 
n = 0
v = ''
num =[ 'p1t1.txt' , 'p1t2.txt' , 'p1t3.txt' , 'p1t4.txt' , 'p1t5.txt' ]

def timerec():
    global element
    driver = webdriver.Chrome(executable_path='/home/piyush/Documents/python/cstimer auto/chromedriver')
    driver.get("https://www.cstimer.net")
    element = driver.find_element_by_id('lcd')

def write():
    global n 
    name = num[n]
    print (name)
    my_file = open(name, 'w')
    my_file.write(str(element.text))
    n += 1
    if n == 4 :
        n == 0
    print(n)
    
def average():
    global v
    p1t1= open('p1t1.txt','r')
    p1t2= open('p1t2.txt','r')
    p1t3= open('p1t3.txt','r')
    p1t4= open('p1t4.txt','r')
    p1t5= open('p1t5.txt','r')
    p1a= open('p1a.txt','w')
    p1a.write(' ')
    x1 = float(p1t1.read())
    x2 = float(p1t2.read())
    x3 = float(p1t3.read())
    x4 = float(p1t4.read())
    x5 = float(p1t5.read())
    v = str(round((x1+x2+x3+x4+x5)/5,2))
    print(x1+x2+x3+x4+x5) 
    print(v ,'v')
    p1a.write(v)
    
def rst():
    global n ,v
    n=0
    v=''
    p1t1= open('p1t1.txt','w')
    p1t2= open('p1t2.txt','w')
    p1t3= open('p1t3.txt','w')
    p1t4= open('p1t4.txt','w')
    p1t5= open('p1t5.txt','w')
    p1a= open('p1a.txt','w')
    p1t1.write('0.00')
    p1t2.write('0.00')
    p1t3.write('0.00')
    p1t4.write('0.00')
    p1t5.write('0.00')
    p1a.write('0.00')
    
    
gui = tkinter.Tk() 
gui.configure(background="light green") 
gui.title("time manager") 
gui.geometry("337x50") 

start = tkinter.Button(gui, text=' start ', fg='black', bg='red',command=lambda:timerec(), height=1, width=7) 
start.grid(row=2, column=0) 

nextTime = tkinter.Button(gui, text=' next time ', fg='black', bg='red',command=lambda:write(), height=1, width=7) 
nextTime.grid(row=2, column=1) 

avg = tkinter.Button(gui, text='avg cal ', fg='black', bg='red',command=lambda:average(), height=1, width=7) 
avg.grid(row=2, column=2) 

rest = tkinter.Button(gui, text='reset ', fg='black', bg='red',command=lambda:rst(), height=1, width=7) 
rest.grid(row=2, column=3) 

gui.mainloop() 
