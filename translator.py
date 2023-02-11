
from tkinter import *
from tkinter import ttk # For Combobox
from googletrans import Translator,LANGUAGES
import pickle
#Translate code
def fun1():
    msg = in_text.get(1.0,END)
    s = c1.get()
    d = c2.get()
    t = Translator()
    t = t.translate(text = str(msg), src=str(s), dest=str(d))
    t = t.text
    # print(t)
    # dict = {}
    # key = f"{msg} ({s})"
    # value =  f"{t} ({d})"
    # dict[key] = value
    with open("history.txt","ab") as f:
        f_in = f"{msg} ({s})--- {t} ({d})\n"
        f.write(f_in.encode(encoding="utf-16"))

    # with open("history1.txt","ab") as f:
    #     pickle.dump(d,f)
    out_text.delete(1.0,END)
    out_text.insert(END,t)

#window
win = Tk() # Tk is a widget creates a new window
win.title("Language Translator")
win.geometry("1000x500")
win.config(bg="aqua")

# main heading
head = Label(win,text="Translator",font="roman 20 bold",bg="green",fg="white")
head.place(x=320,y=20,width=300,height=30)

# input heading
in_head = Label(win,text="Input Text",font="italic 15 bold",bg="green",fg="white")
in_head.place(x=50,y=90,width=200,height=30)

# input frame (box) for input
in_text = Text(font="roman 20 bold")
in_text.place(x=10,y=160,width=350,height=80)
#input language combobox
sel_lang =Label(win, text="select >>>",font="italic 15 bold",bg="green",fg="white")
sel_lang.place(x=50,y=130,width=100,height=20)
c1= ttk.Combobox(value= list(LANGUAGES.values()))
c1.place(x=170,y=130,width=100,height=20)
c1.set("English")
#Button
b = Button(text="Translate",bg="violet",fg="white",font='roman 15 bold',command=fun1)
b.place(x=415,y=180,width=120,height=30)
#output heading
out_h = Label(win,text="Translated Text",font="italic 15 bold",bg="green",fg="white")
out_h.place(x=650,y=90,width=200,height=30)
# output frame (box) for input
out_text = Text(font="roman 20 bold")
out_text.place(x=600,y=160,width=350,height=80)
#output language combobox
sel_lan =Label(win, text="select >>>",font="italic 15 bold",bg="green",fg="white")
sel_lan.place(x=650,y=130,width=100,height=20)
c2= ttk.Combobox(value= list(LANGUAGES.values()))
c2.place(x=770,y=130,width=100,height=20)
c2.set("Telugu")

win.mainloop()
