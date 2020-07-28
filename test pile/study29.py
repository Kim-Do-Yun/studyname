from tkinter import*

num = 0

def vv():
    global num
    num += int(c.get())
    b["text"] = str(num)

def bb():
    global num
    num -= int(c.get())
    b["text"] = str(num)

def nn():
    global num
    num = 0
    b["text"] = str(num)
    c.delete(0, END)

window = Tk()
a = Label(window, text = "현재 합계")
b = Label(window, text = "0")
c = Entry(window)
d = Button(window, text = "더하기(+)", command = vv)
e = Button(window, text = "빼기(-)", command = bb)
f = Button(window, text = "초기화", command = nn)

a.grid(row = 0, column = 0)
b.grid(row = 0, column = 1, columnspan = 2)
c.grid(row = 1, column = 0, columnspan = 3)
d.grid(row = 2, column = 0)
e.grid(row = 2, column = 1)
f.grid(row = 2, column = 2)

window.mainloop()

#print(eval("2+3-6"))