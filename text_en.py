from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
import os

s='1.0'
root = Tk()
root.title('notes')
root.geometry('400x400')


        
def zapusk(gg):
        rooot=Tk()
        ccc=text.get(s, END)
        
        print(ccc)
        
        ff=(exec(ccc))
        
        
        print('>>>',end='')
        def c():exec(ccc)
        Label(rooot,text=c()).pack()
        rooot.mainloop()
def save_no_file():
        out = open("text.txt","w")
        out.write(text.get(s, END))
        out.close()
        


def new_file():
        global file_name
        file_name = "Untitled"
        text.delete(1.0, END)
def save_file():pass
def help_my():
        from tkinter import messagebox  
      
      
        #def clicked():  
        messagebox.showinfo('help', 'this app is version 2.0.0')
def save(txt):
        u='.'+txt
        out = asksaveasfile(mode='w', defaultextension=u)
        data = text.get(s, END)
        try:
            out.write(data.rstrip())
        except Exception:
            messagebox.showerror("Oh! Not good ... "," I gave you false hope ... The file cannot be saved!")

def save_as():
        roott=Tk()
        txt = Entry(roott,width=10)  
        txt.pack()
        Button(roott,text='send',command=lambda:save(txt.get())).pack()
        

def open_file():
        global file_name
        inp = askopenfile(mode = 'r')
        if inp is None:
            return
            file_name = inp.name
        data = inp.read()
        text.delete(s, END)
        text.insert(s, data)
def open1():

    #import tkinter as tk
    import tkinter.filedialog as fd
    import webbrowser as web
    

    filetypes = (("html", "*.html"),
                 ("Любой", "*"))
    filename = fd.askopenfilename(title="open file", initialdir="/",
                                  filetypes=filetypes)
    
    web.open_new_tab('file:///'+filename)

    
def zapusk_html():
    
   
    open1()
    
while True:
    def html():
        messagebox.showinfo('write', 'write html')
        save_as()
        p=run_menu.add_command(label="execute html",command=zapusk_html)
        
    def zapusk_js():
        print(text.get(s, END))
        import js2py
        f = js2py.eval_js( text.get(s, END) )
        
        print('>>>')
    def python():
        #if not p:
        #print(text.get(s, END))
        p=run_menu.add_command(label="execute python",command=lambda:zapusk(text.get(s, END)))
        
        
    Button(root,text='put into python programming mode',command=python).pack()
    Button(root,text='put into html programming mode',command=html).pack()
    def js():
        
        j=run_menu.add_command(label="execute js",command=zapusk_js)
        

    Button(root,text='put into js programming mode',command=js).pack()
    text = Text(root,width=400, height=400)
    text.pack()

    menu_bar = Menu(root)
    file_menu = Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label='file', menu = file_menu)
    help_menu = Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label='help', menu = help_menu)
    run_menu = Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label='run', menu = run_menu)
    rn_menu = Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label='exit', menu = rn_menu)
    file_name = NONE
    
    import sys
    file_menu.add_command(label="new file",command=new_file)
    file_menu.add_command(label="save as...", command=save_as)
    file_menu.add_command(label="save", command=save_no_file)
    file_menu.add_command(label="open",command=open_file)
    rn_menu.add_command(label="exit",command=sys.exit)
    help_menu.add_command(label="version of the note",command=help_my)
    root.config(menu=menu_bar)
    
    root.mainloop()
    #python-3.x
# STEP project
