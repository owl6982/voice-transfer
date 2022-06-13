from tkinter import *
import os
from tkinter import filedialog
import tkinter.messagebox
import openpyxl

import time
import tkinter as tk


root = Tk()


def transfer():
    text.delete(1.0, END)
    import voide_transfer
    voide_transfer.vtransfer(text=text)


def record():
    text.delete(1.0, END)
    from voice_record import recoder
    r = recoder()
    r.recoder()
    r.savewav("16k.wav")
    return tkinter.messagebox.showinfo('hint','recording end')




b1 = Button(root, text="record" , command=record, width=10, height=3).grid(row=1, column=0)
b2 = Button(root, text="translate" , command=transfer, width=10, height=3).grid(row=1, column=1)
text = Text(root, width=50, height=60)
text.grid(row=2, column=0, columnspan=2)


mainloop()
