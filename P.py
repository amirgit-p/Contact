from tkinter import *
from tkinter import messagebox
from class_db import Database
win = Tk()
win.geometry('685x400')
win.resizable(0,0)
win.title('P')
win.configure(bg='light blue')
#----------------------Functons---------------------
db = Database('E:/db/mydb.db')
def add_item():
    if ent_fname.get() == '' or ent_lname.get() == '' or ent_address.get() == '' or ent_phone.get() == '':
        messagebox.showerror('ERROR', 'fill all of the textbox')
        return
    db.insert(ent_fname.get(), ent_lname.get(), ent_address.get(), ent_phone.get())


def clear():
    ent_address.delete(0, END)
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_phone.delete(0,END)

def show_list():
    lst.delete(0,END)
    for i in db.fetch():
        lst.insert(END , f'{i[0]} , {i[1]} , {i[2]} , {i[3]} , {i[4]}')
def delete_():
    index = lst.curselection()
    data = lst.get(index)
    datamain = data.split(',')
    db.remove(datamain[0])
    lst.delete(index)
    
def update():
    index = lst.curselection()
    data = lst.get(index)
    datamain = data.split(',')
    db.update(datamain[0] , ent_fname.get() , ent_lname.get() , ent_address.get() , ent_phone.get())
def search():
    pass
def select_item(event):
    index = lst.curselection()
    data = lst.get(index)
    x= data.split(',')
    clear()
    ent_fname.insert(END, x[1])
    ent_lname.insert(END , x[2])
    ent_address.insert(END, x[3])
    ent_phone.insert(END, x[4])
def exit_():
    win.destroy()

#----------------------Widgets----------------------

lbl_fname = Label(win , text='Fname :' , font='arial 15 bold' , bg='light blue')
lbl_fname.place(x=10 ,y=10)
ent_fname = Entry(win ,font='arial 15 bold')
ent_fname.place(x=105 ,y=10)
lbl_lname = Label(win , text='Lname :' , font='arial 15 bold' ,bg='light blue')
lbl_lname.place(x=350 ,y=10)
ent_lname = Entry(win , font='arial 15 bold')
ent_lname.place(x=445 ,y=10)
lbl_address = Label(win , text='Address:' ,font='arial 15 bold' ,bg='light blue')
lbl_address.place(x=10 ,y=55)
ent_address = Entry(win ,font='arial 15 bold')
ent_address.place(x=105 ,y=55)
lbl_phone = Label(win , text='Phone :' ,font='arial 15 bold' ,bg='light blue')
lbl_phone.place(x=350 ,y=55)
ent_phone = Entry(win , font='arial 15 bold')
ent_phone.place(x=445 ,y=55)
lst = Listbox(win , font='arial 10 bold' ,width=93)
lst.place(x=13 ,y=100)
scorllbr = Scrollbar(win)
scorllbr.place(x=650 ,y=102 ,height=170)
lst.config(yscrollcommand= scorllbr.set)
scorllbr.config(command=lst.yview)
btn_insert = Button(win ,text='Insert' ,font='arial 13 bold' ,width=15,command=add_item)
btn_insert.place(x=13 ,y=280)
btn_clear = Button(win ,text='Clear' ,font='arial 13 bold' ,width=15 ,command=clear)
btn_clear.place(x=180 ,y=280)
btn_delete = Button(win ,text='Delete' ,font='arial 13 bold' ,width=15,command=delete_)
btn_delete.place(x=345 ,y=280)
btn_update = Button(win ,text='Update' ,font='arial 13 bold' ,width=15 ,command=update)
btn_update.place(x=510 ,y=280)
btn_search = Button(win ,text='Search' ,font='arial 13 bold' ,width=15 ,command=search)
btn_search.place(x=13 ,y=320)
ent_search = Entry(win ,font='arial 17 bold' ,width=25)
ent_search.place(x=177 ,y=321)
btn_exit = Button(win ,text='Exit' ,font='arial 13 bold' ,width=15 ,command=exit_)
btn_exit.place(x=510,y=321)
btn_slct = Button(win , text='Show info' , font='arial 13 bold' , width=65 , command=show_list)
btn_slct.place(x=13 , y=360)
lst.bind('<<ListboxSelect>>' ,select_item)
win.mainloop()