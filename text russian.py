from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
import os

s='1.0'
root = Tk()
root.title('Заметки')
#root.geometry('400x400')
def zapusk_js():
    import js2py
    f = js2py.eval_js( text.get(s, END) )
    try:
        f
        #i=True
    except:
        print("error")
    

def python():
    file_menu.add_command(label="выполнить python",command=zapusk)
    
Button(root,text='перевод в режим программирования python',command=python).pack()
def js():
    
    file_menu.add_command(label="выполнить js",command=zapusk_js)
    

Button(root,text='перевод в режим программирования js',command=js).pack()
def clear():
    #text.get(s, END).configure()
    text.delete("1.0","end")
     
Button(root,text='очистить',command=clear).pack()
text = Text(root,width=400, height=400)
text.pack()
    


menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label='Файл', menu = file_menu)
help_menu = Menu(menu_bar)
menu_bar.add_cascade(label='помощь', menu = help_menu)

file_name = NONE
def zapusk():
    сс=text.get(s, END)
    exec(сс)
def save_no_file():
    out = open("text.txt","w")
    out.write(text.get(s, END))
    out.close()
    


def new_file():
    global file_name
    file_name = "Без названия"
    text.delete(1.0, END)
def save_file():pass
def help_my():
    from tkinter import messagebox  
  
  
    #def clicked():  
    messagebox.showinfo('помощь', 'это приложение версии 1.3.6')
def save(txt):
    u='.'+txt
    out = asksaveasfile(mode='w', defaultextension=u)
    data = text.get(s, END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Ой!Не хорошо...","Я дал тебе ложную  надежду...Файл нельзя ссохранить!")

def save_as():
    roott=Tk()
    txt = Entry(roott,width=10)  
    txt.pack()
    Button(roott,text='отправить',command=lambda:save(txt.get())).pack()
    

def open_file():
    global file_name
    inp = askopenfile(mode = 'r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete(s, END)
    text.insert(s, data)

file_menu.add_command(label="Новый",command=new_file)
file_menu.add_command(label="Сохранить как...", command=save_as)
file_menu.add_command(label="Сохранить", command=save_no_file)
file_menu.add_command(label="Открыть",command=open_file)

help_menu.add_command(label="помощь заметки",command=help_my)
root.config(menu=menu_bar)
root.mainloop()
#python-3.x
