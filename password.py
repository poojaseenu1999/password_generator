from tkinter import*
import random,string

root=Tk()
#root.geometry("400X280")
root.title("password_generator")

title=StringVar()
label=Label(root,textvariable=title).pack()
title.set("the strength of password")

def selection():
    selection=choice.get()
choice=IntVar()
r1=Radiobutton(root,text='POOP',variable=choice,value=1,command=selection).pack(anchor=CENTER)
r2=Radiobutton(root,text='AVERAGE',variable=choice,value=2,command=selection).pack(anchor=CENTER)
r3=Radiobutton(root,text='STRONG',variable=choice,value=3,command=selection).pack(anchor=CENTER)

labelchoice=Label(root).pack()

lenlabel=StringVar()
lenlabel.set("password length")
lentitle=Label(root,textvariable=lenlabel).pack()

val=IntVar()
spinlength=Spinbox(root,from_=8, to_=24,textvariable=val,width=13).pack()

def callback():
     Isum.congif(text=passgen())


passgenButton=Button(root,text="Generate password",bd=5,height=2,command=callback,pady=3)
passgenButton.pack()
password=str(callback)




poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_uppercase+string.ascii_lowercase+string.digits
symbols='\~!@$%^&*()_+-={}[]|:;<>,.?/'
advance=poor+average+symbols

def passgen():
    if choice.get()==1:
        return "".join(random.sample(poor,val.get()))
    if choice.get()==2:
            return "".join(random.sample(average,val.get()))
    if choice.get()==3:
            return "".join(random.sample(strong,val.get()))


root.mainloop()
