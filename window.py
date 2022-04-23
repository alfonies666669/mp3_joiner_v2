import tkinter
from tkinter import *
from tkinter import Menu
from tkinter import ttk

root = Tk()
content = ttk.Frame(root, padding=(3, 3, 12, 12))

# Main window
root['bg'] = '#fafafa'
png = tkinter.PhotoImage(file='free-icon-mp3-457681.png')
root.iconphoto(True, png)
root.title('Easy mp3 Joiner')
root.wm_attributes('-alpha', 0.7)
root.minsize(500, 480)
root.geometry('500x480+400+100')

# Top menu
root.option_add('*tearOff', FALSE)
menu = Menu(root)
new_item = Menu(menu)
new_item.add_command(label='Открыть . . . ')
new_item.add_command(label='Закрыть')
new_item.add_separator()
new_item.add_command(label='Выход')
menu.add_cascade(label='Файл', menu=new_item)

support = Menu(menu)
support.add_command(label='О программе')
menu.add_cascade(label='Справка', menu=support)
root.config(menu=menu)

# Buttons
ok = ttk.Button(content, text="Отменить")
cancel = ttk.Button(content, text="OK")
content.grid(column=0, row=0, sticky=(N, S, E, W))
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.rowconfigure(1, weight=1)

# Process bar
p = ttk.Progressbar(root, orient=HORIZONTAL, length=680, mode='determinate')
p.grid(column=0, row=0, columnspan=20, padx=10, pady=20)

root.mainloop()
