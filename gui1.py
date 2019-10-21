
from tkinter import * 
import tkinter.messagebox

def custom_quit():
    ans=tkinter.messagebox.askokcancel(title="Are you sure?",message="data may be lost")
    if (ans):
        quit()

def work():
    print("Its working")
def res():
    print("GUI window resized")
    root.geometry("200x100")
def norm():
    print("GUI window back to normal")
    root.geometry("400x300")
    
root=Tk()
root.geometry("400x400")
menu_1=Menu(root)
root.config(menu=menu_1)

file_menu=Menu(menu_1)
menu_1.add_cascade(label="file",menu=file_menu)

file_menu.add_command(label="newfile",command=work)
file_menu.add_cascade(label="open")
file_menu.add_cascade(label="save")
file_menu.add_cascade(label="save as")
file_menu.add_cascade(label="exit")

view_menu=Menu(menu_1)
menu_1.add_cascade(label="view",menu=view_menu)

run_menu=Menu(menu_1)
menu_1.add_cascade(label="run",menu=run_menu)

edit_menu=Menu(menu_1)
menu_1.add_cascade(label="edit",menu=edit_menu)
edit_menu.add_command(label="resized",command=res)
edit_menu.add_command(label="normal",command=norm)
edit_menu.add_cascade(label="cut")
edit_menu.add_cascade(label="paste")
edit_menu.add_cascade(label="exit")


search_menu=Menu(menu_1)
menu_1.add_cascade(label="search",menu=search_menu)
help_menu=Menu(menu_1)
menu_1.add_cascade(label="help",menu=help_menu)

status=Label(root,text="run",anchor="n",relief=SUNKEN,bg="blue",bd=1)
status.pack(side=BOTTOM,fill=X)

root.mainloop()

