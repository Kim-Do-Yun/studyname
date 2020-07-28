from tkinter import*

window = Tk()

a = Label(window, text="화씨")
b = Label(window, text="섭씨")
c = Entry(window)
d = Entry(window)
e = Button(window, text="화씨->섭씨")
f = Button(window, text="섭씨->화씨")
a.pack()
b.pack()
c.pack()
d.pack()
e.pack()
f.pack()

window.mainloop()