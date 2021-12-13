import tkinter as tk
from tkinter import  *

window =tk.Tk()
dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label1.grid(row=1, column=1, sticky=E)
text1 = tk.Label(window, text="Pochacco!")
text1.grid(row=1, column=2, sticky=W)
label2 = tk.Label(window, text="A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", borderwidth=1, bg="#A3FFFF")
label2.grid(row=2, column=1, columnspan=2)













window.mainloop()
