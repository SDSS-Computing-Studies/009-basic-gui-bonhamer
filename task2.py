import tkinter as tk
from tkinter import  *

window = tk.Tk()
window.title("T-Town Veterinary Database ")
dogphoto = PhotoImage(file="dog.png")



label1 = tk.Label(window,text="Client Database")
label2 = tk.Label(window, image=dogphoto, borderwidth=1)
label5 = tk.Label(window,text="Name")
label6 = tk.Label(window,text="Type")
label7 = tk.Label(window,text="Breed")
label8 = tk.Label(window,text="Owner")
label9 = tk.Label(window,text="Birthdate")
label1.grid(row = 1, column = 2)
label2.grid(row = 1, column = 0, sticky=NE)
label5.grid(row = 2, column = 0)
label6.grid(row = 2, column = 1)
label7.grid(row = 2, column = 2)
label8.grid(row = 2, column = 3)
label9.grid(row = 2, column = 4)
Text1 = tk.Entry(window, borderwidth=2)
Text2 = tk.Entry(window, borderwidth=2)
Text3 = tk.Entry(window, borderwidth=2)
Text4 = tk.Entry(window, borderwidth=2)
Text5 = tk.Entry(window, borderwidth=2)
Text6 = tk.Entry(window, borderwidth=2)
Text1.grid(row=3, column = 0)
Text2.grid(row=3, column = 1)
Text3.grid(row=3, column = 2)
Text4.grid(row=3, column = 3)
Text5.grid(row=3, column = 4)
Text6.grid(row=0, column = 4)
button1 = tk.Button(window,text="BONISBESTCODERNAW")
button2 = tk.Button(window,text="<Previous")
button3 = tk.Button(window,text="Next>")
button4 = tk.Button(window,text="Search By Name")
button1.grid(row = 4, column = 2)
button2.grid(row = 4, column = 0)
button2.grid(sticky=W)
button3.grid(row = 4, column = 4)
button3.grid(sticky=E)
button4.grid(row = 0, column = 3)
button4.grid(sticky=E)


window.mainloop()