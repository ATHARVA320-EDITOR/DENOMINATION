from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Denomination calculator")
root.configure(bg = 'light blue')
root.geometry = ('650x400')
upload = Image.open("img.jpeg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=100, y=20)
label1 = Label(root,
               text="Hey user!Welcome to denomination calculator app.",
               bg='light blue')
label1.place(relx= 0.5, y= 340, anchor=CENTER)
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination?")
    if MsgBox == 'ok':
        topwin()
