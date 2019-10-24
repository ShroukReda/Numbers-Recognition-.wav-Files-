import tkinter as tk
from tkinter import *
import time


def Start(event=None):
    time.sleep(5)
    UserInput=Answer.set("mangain ram kernel job")  # badl da 7otly l predicted output
    return UserInput #nnady 3ala function nb3tlha l input w trg3 l output n7oto x Answer.set

def test(event=None):
    time.sleep(20)
    a=accur.set("73.0")
    return a  #nnady 3ala function nb3tlha l input w trg3 l output n7oto x Answer.set

root = tk.Tk()
root.geometry('800x400+200+400')
root.configure(background="black")
root.title('Technical Support Chatbot For Ubuntu Problems')
UserQuestion= tk.StringVar()
Answer=tk.StringVar()
accur=tk.StringVar()
labelTitle = tk.Label(root,font="Helvetica 18 bold",bg="blue",width=30,text="Welcome To Our Chatbot :)").place(x=180,y=30)
label1 = tk.Label(root, font="Helvetica 18 bold", bg="black",fg="gray",text="Ask A Question!").place(x=300,y=100)
labelResult = tk.Label(root)
T = Entry(root,font="Helvetica 15",textvariable=UserQuestion,bg="gray",fg="black",highlightbackground="black",highlightcolor="red",highlightthickness=1,bd=5, width=27).place(x=250,y=130)
Response = Entry(root, textvariable=Answer,font="Helvetica 15  bold",bg="gray",fg="black",highlightbackground="black",highlightcolor="red",highlightthickness=1,bd=5,width=27).place(x=250,y=210)
ConvStarter = tk.Button(root, text="Start Chatting",width=20,font="Helvetica 10 bold", bg="black",fg="gray", command=Start).place(x=320,y=260)
acc = Entry(root, textvariable=accur,font="Helvetica 15  bold",bg="gray",fg="black",highlightbackground="black",highlightcolor="red",highlightthickness=1,bd=5,width=8).place(x=350,y=300)
Test = tk.Button(root, text="Test",width=20,font="Helvetica 10 bold", bg="black",fg="gray", command=test).place(x=320,y=350)
root.mainloop()