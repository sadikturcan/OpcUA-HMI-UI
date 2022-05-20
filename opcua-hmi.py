from opcua import Client
import time
from tkinter import*
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import threading



 
def opcuaconnection(url,enteredsec,rvalue2):

    
    myurl="opc.tcp://"
    myurl+=url
    xvalues=0
    global status
    status=True
    
        
        
    client = Client(myurl)
    client.connect()
    print("connected")
    fieldnames=["xvalues","Tag1plot","Tag2plot","Tag3plot","Tag4plot","Tag5plot"]
    with open('data.csv','w') as csv_file:
        csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
        csv_writer.writeheader() 
    
    button = Button(frameust,width=20,text = "Stop",font="Verdana 12",command=stopbutton)
    button.place(x=120,y=6,height=30,width=100)
    

    while (status==True):
       
        
        Tag1=client.get_node("ns=3;s=Tag1")

        Tag1value.set(Tag1.get_value())
        print("Tag1 ={}".format(Tag1value.get()))

        Tag2=client.get_node("ns=3;s=Tag2")

        Tag2value.set(Tag2.get_value())
        print("Tag2={}".format(Tag2value.get()))

        Tag3=client.get_node("ns=3;s=Tag3")

        Tag3value.set(Tag3.get_value())
        print("Tag3={}".format(Tag3value.get()))

        Tag4=client.get_node("ns=3;s=Tag4")

        Tag4value.set(Tag4.get_value())
        print("Tag4={}".format(Tag4value.get()))

        Tag5=client.get_node("ns=3;s=Tag5")
            
        Tag5value.set(Tag5.get_value())
        print("Tag5={}".format(Tag5value.get()))

        print("-------------------------")
        
        Tag1ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",textvariable=Tag1value)
        Tag1ValueLabel.place(x=50,y=100)
        Tag2ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",textvariable=Tag2value)
        Tag2ValueLabel.place(x=50,y=140)
        Tag3ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",textvariable=Tag3value)
        Tag3ValueLabel.place(x=50,y=180)
        Tag4ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",textvariable=Tag4value)
        Tag4ValueLabel.place(x=50,y=220)
        Tag5ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",textvariable=Tag5value)
        Tag5ValueLabel.place(x=50,y=260)
        with open('data.csv','a') as csv_file:
            csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
            info={
                "xvalues":xvalues,
                "Tag1plot":Tag1value.get(),
                "Tag2plot":Tag2value.get(),
                "Tag3plot":Tag3value.get(),
                "Tag4plot":Tag4value.get(),
                "Tag5plot":Tag5value.get()
            }
            csv_writer.writerow(info)
            animate(rvalue2)
            xvalues+=1
            
            
            
        
        
        
        
        time.sleep(float(enteredsec))
        
        master.update()
    
    

            
        

      
           
        

       
master= Tk()
master.title("OPCUA-HMI")
canvas = Canvas(master,height=600,width=1000,bg="lightblue")
canvas.pack()



frameust=Frame(master,bg="lightblue")
frameust.place(relx=0,rely=0.08,relwidth=0.8,relheight=0.2)
framealt=Frame(master,bg="white")
framealt.place(relx=0,rely=0.3,relwidth=1,relheight=0.99)
Tag1ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",text="")
Tag1ValueLabel.place(x=50,y=100)
Tag2ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",text="")
Tag2ValueLabel.place(x=50,y=140)
Tag3ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",text="")
Tag3ValueLabel.place(x=50,y=180)
Tag4ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",text="")
Tag4ValueLabel.place(x=50,y=220)
Tag5ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",text="")
Tag5ValueLabel.place(x=50,y=260)
Tag1value=StringVar()
Tag2value=StringVar()
Tag3value=StringVar()
Tag4value=StringVar()
Tag5value=StringVar()
fig=Figure()
ax=fig.add_subplot(111)
ax.set_title("TAGS")
ax.set_xlabel("Sample Count")
ax.set_ylabel("Tag Values")
ax.set_xlim(0,20)
ax.set_ylim(0,120)



lines=ax.plot([],[])[0]

    


canvas=FigureCanvasTkAgg(fig,master=framealt)
canvas.get_tk_widget().place(x=400,width=600,height=400)
canvas.draw()

serveradress=Label(frameust,bg="white",text="Server Adress",font="Verdana 12")
serveradress.pack(padx=5,pady=5,side=LEFT)
connectstatus=Label(frameust,bg="lightgreen",text="Connected",font="Verdana 12")
nameEntered =Entry(frameust,width=20,font=" Verdana 12 bold")
nameEntered.pack(side=LEFT)
refreshfreq=Label(frameust,bg="white",text="Refresh Rate",font="Verdana 12")
refreshfreq.place(x=0,y=100)
enteredsecond=Entry(frameust,width=8,font="Verdana 12 bold")
enteredsecond.place(x=127,y=100)
r=StringVar()
r.set('Tag5plot')
myseconds=1
print(r.get())
button = Button(frameust,width=20,text = "Enter",font="Verdana 12",command=lambda:[connectstatus.pack(padx=5,pady=5,side=RIGHT),opcuaconnection(nameEntered.get(),enteredsecond.get(),r.get())])
button.place(x=5,y=6,height=30,width=100)
Radiobutton(framealt,text="Tag1",variable=r,value='Tag1plot').place(x=300,y=100)
Radiobutton(framealt,text="Tag2",variable=r,value='Tag2plot').place(x=300,y=140)
Radiobutton(framealt,text="Tag3",variable=r,value='Tag3plot').place(x=300,y=180)
Radiobutton(framealt,text="Tag4",variable=r,value='Tag4plot').place(x=300,y=220)
Radiobutton(framealt,text="Tag5",variable=r,value='Tag5plot').place(x=300,y=260)


def animate(rvalue):
    plt.cla()
    data=pd.read_csv('data.csv')
    x=data['xvalues']
    y1=data['Tag1plot']
    y2=data['Tag2plot']
    y3=data['Tag3plot']
    y4=data['Tag4plot']
    y5=data['Tag5plot']
    
    plt.plot(x,y1,label='Tag1')
    plt.plot(x,y2,label='Tag2')
    plt.plot(x,y3,label='Tag3')
    plt.plot(x,y4,label='Tag4')
    plt.plot(x,y5,label='Tag5')
    
    if(rvalue=='Tag1plot'):
        lines.set_xdata(x)
        lines.set_ydata(y1)
        canvas.draw()
    elif(rvalue=='Tag2plot'):
        lines.set_xdata(x)
        lines.set_ydata(y2)
        canvas.draw()
    elif(rvalue=='Tag3plot'):
        lines.set_xdata(x)
        lines.set_ydata(y3)
        canvas.draw()
    elif(rvalue=='Tag4plot'):
        lines.set_xdata(x)
        lines.set_ydata(y4)
        canvas.draw()
    elif(rvalue=='Tag5plot'):
        lines.set_xdata(x)
        lines.set_ydata(y5)
        canvas.draw()
    



    
    
    
def stopbutton():
    global status
    status=False
    Tag1ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",text="")
    Tag1ValueLabel.place(x=50,y=100)
    Tag2ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",text="")
    Tag2ValueLabel.place(x=50,y=140)
    Tag3ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",text="")
    Tag3ValueLabel.place(x=50,y=180)
    Tag4ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",text="")
    Tag4ValueLabel.place(x=50,y=220)
    Tag5ValueLabel=Label(framealt,width=10,bg="lightgray",font=" Verdana 12 bold",borderwidth=2,relief="solid",text="")
    Tag5ValueLabel.place(x=50,y=260)
    connectstatus.pack_forget()
      

master.mainloop() 







   
    


