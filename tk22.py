#-*- coding: utf-8 -*-
#tk21.pyw

import tkinter as tk
def return_press(event):
    en_val = strvar.get()
    printer(en_val)

strvar.set(" ")
root = tk.Tk()
strvar = tk.StringVar()
en = tk.Entry(textvariable=strvar)
en.bind("<Return>",return_press)
en.pack()
root.mainloop()