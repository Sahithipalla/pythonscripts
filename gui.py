from tkinter import *



def subscribe():
    print("joining to learn python")
    
root=Tk()
root.geometry("400x400")
button_1=Button(root,text="join now",command=subscribe)
button_1.pack()
button_2=Button(root,text="Exit",command=root.quit)
button_2.pack()
root.mainloop()

def left(event):
    print("you have clicked on left mouse button")
def right(event):
    print("you have clicked on right mouse button")
root=Tk()
root.geometry("400x400")
frame=Frame(root,width=400,height=400)
frame.bind("<Button-1>",left)
frame.bind("<Button-3>",right)
frame.pack()
root.mainloop()



def work():
    print("Its working")
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

search_menu=Menu(menu_1)
menu_1.add_cascade(label="search",menu=search_menu)


root.mainloop()