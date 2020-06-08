from tkinter import *
from tkinter import ttk
from tkinter import messagebox

"""
    Este código é de experimentação, não tem função devidamente implementada e não
    está sendo aplicado com o projeto na raiz do projeto.

    O código está poluído com um amontoado de estilos de construção e por vezes o
    chamado de uma é morto pra que se possa testar a outra.

    O Tkinter não é uma biblioteca que eu use e por isso preciso entender como ela
    trabalha.
"""

window = Tk()


def principal():

    window.title('Teste de título primário')
    window.geometry('500x500')

    btn1 = Button(window,text='Me clique', command=clicked)
    btn2 = Button(window, text='Me clique 2', command=secundaria)

    btn1.grid(column=0,row=0)
    btn2.grid(column=2,row=2)

def secundaria():

    window.title('Teste de título secundário')
    window.geometry('500x500')

    btn1 = Button(window,text='Me clique para testar', command=clicked)

    btn1.grid(column=0,row=0)



def clicked():

    messagebox.showinfo('Message title', 'Message content')

    messagebox.askyesnocancel('Message title','Message content')

    messagebox.askyesno('Título','Contexto')

    # OK/YES/RETRY -> RETURNS TRUE BOOL
    # NO/CANCEL -> RETURNS FALSE BOOL

LARGEFONT =("Verdana", 35) 
   
class tkinterApp(Tk.Tk): 
      
    # __init__ function do tkinterapp
    def __init__(self, *args, **kwargs):  
          
        # __init__ do Tk
        Tk.Tk.__init__(self, *args, **kwargs) 
          

        container = Tk.Frame(self)   
        container.pack(side = "top", fill = "both", expand = True)  
   
        container.grid_rowconfigure(0, weight = 1) 
        container.grid_columnconfigure(0, weight = 1) 
   

        self.frames = {}   
   

        for F in (MainPage, Pagina1, Pagina2): 
   
            frame = F(container, self) 
   
            self.frames[F] = frame  
   
            frame.grid(row = 0, column = 0, sticky ="nsew") 
   
        self.show_frame(MainPage) 
   

    def show_frame(self, cont): 
        frame = self.frames[cont] 
        frame.tkraise() 
   

   
class MainPage(Tk.Frame): 
    def __init__(self, parent, controller):  
        Tk.Frame.__init__(self, parent) 
          


        label = ttk.Label(self, text ="Startpage", font = LARGEFONT) 
          


        label.grid(row = 0, column = 4, padx = 10, pady = 10)  
   
        button1 = ttk.Button(self, text ="Page 1", 
        command = lambda : controller.show_frame(Pagina1)) 
      


        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
   


        button2 = ttk.Button(self, text ="Page 2", 
        command = lambda : controller.show_frame(Pagina2)) 



        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
   
           
   
   
# second window frame page1  
class Pagina1(Tk.Frame): 
      
    def __init__(self, parent, controller): 
          
        Tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Pagina 1", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
   


        button1 = ttk.Button(self, text ="Main", 
                            command = lambda : controller.show_frame(MainPage)) 


        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
   

        button2 = ttk.Button(self, text ="Pagina 2", 
                            command = lambda : controller.show_frame(Pagina2)) 
      

        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
    


class Pagina2(Tk.Frame):  
    def __init__(self, parent, controller): 
        Tk.Frame.__init__(self, parent) 
        label = ttk.Label(self, text ="Pagina 2", font = LARGEFONT) 
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
   
        # button to show frame 2 with text 
        button1 = ttk.Button(self, text ="Pagina 1", 
                            command = lambda : controller.show_frame(Pagina1)) 
      
        # alocando o button
        button1.grid(row = 1, column = 1, padx = 10, pady = 10) 
   
        # button que dá trigger no frame 3 
        button2 = ttk.Button(self, text ="Main", 
                            command = lambda : controller.show_frame(MainPage)) 
      
        # alocando o button
        button2.grid(row = 2, column = 1, padx = 10, pady = 10) 
   
   
# Triggers
app = tkinterApp()
window.mainloop()