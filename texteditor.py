#simple text editor
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import tkinter.scrolledtext

root=Tk(className="simple  Text Editor")
textpad=scrolledtext.ScrolledText(root,width=60,height=600)
def open_command():
    file=filedialog.askopenfile(parent=root,mode="rb",title="Select a file")
    if file!=None:
        contents=file.read()
        textpad.insert("1.0",contents)
        file.close()
def save_command():
    file=filedialog.asksaveasfile(mode="w")
    if file!=None:
        data=textpad.get("1.0",END+"-1c")
        file.write(data)
def exit_command():
    if messagebox.askokcancel("QUIT","do you really want to quit?"):
        root.destroy()
def about_command():
    label=messagebox.showinfo("About","This is Sample Text Editor is created for python")
def work():
    print("Its working")
def res():
    print("GUI window resized")
    root.geometry("200x100")
def norm():
    print("GUI window back to normal")
    root.geometry("400x300")
menu_1=Menu(root)
root.config(menu=menu_1)

file_menu=Menu(menu_1)
menu_1.add_cascade(label="file",menu=file_menu)

file_menu.add_command(label="newfile",command=work)
file_menu.add_command(label="open",command=open_command)
file_menu.add_command(label="save",command=save_command)
file_menu.add_cascade(label="save as")
file_menu.add_command(label="exit",command=exit_command)

view_menu=Menu(menu_1)
menu_1.add_cascade(label="view",menu=view_menu)
view_menu.add_command(label="About",command=about_command)

run_menu=Menu(menu_1)
menu_1.add_cascade(label="run",menu=run_menu)

edit_menu=Menu(menu_1)
menu_1.add_cascade(label="edit",menu=edit_menu)
edit_menu.add_command(label="resized",command=res)
edit_menu.add_command(label="normal",command=norm)
edit_menu.add_cascade(label="cut")
edit_menu.add_cascade(label="paste")
edit_menu.add_cascade(label="exit")

help_menu=Menu(menu_1)
menu_1.add_cascade(label="help",menu=help_menu)

status=Label(root,text="run",relief=SUNKEN,bg="blue",bd=1)
status.pack(side=BOTTOM,fill=X)
textpad.pack()


root.mainloop()


