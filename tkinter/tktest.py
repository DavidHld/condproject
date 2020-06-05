from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()


def principal():

    window.title('Para de rir alek garaio')
    window.geometry('500x500')

    btn1 = Button(window,text='Click here', command=clicked)
    btn2 = Button(window, text='Click 2', command=secundaria)

    btn1.grid(column=0,row=0)
    btn2.grid(column=2,row=2)

def secundaria():

    window.title('JanSec')
    window.geometry('500x500')

    btn1 = Button(window,text='Test SecJan', command=clicked)

    btn1.grid(column=0,row=0)



def clicked():

    messagebox.showinfo('Message title', 'Message content')

    messagebox.askyesnocancel('Message title','Message content')

    messagebox.askyesno('Message','Salve')

    # OK/YES/RETRY -> RETURNS TRUE BOOL
    # NO/CANCEL -> RETURNS FALSE BOOL


principal()

window.mainloop()