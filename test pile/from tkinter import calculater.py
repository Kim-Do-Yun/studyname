from tkinter import *

def click(key) :
    if key == "=" :
        result = eval(display.get())
        display.insert(END, "=" + str(result))
    elif key == "C" :
        display.delete(0, END)
    else :
        display.insert(END, key)


window = Tk()

display = Entry(window, bg="yellow")
display.grid(row=0, column=0, columnspan = 5)

button_list = ['7', '8', '9', '/', 'C',
                '4', '5', '6', '*', ' ',
                '1', '2', '3', '-', ' ',
                '0', '.', '=', '+', ' ']

row_index = 1
col_index = 0

for button_text in button_list :
    def process(t = button_text) :
        click(t)
    Button(window, text=button_text, width=5, command=process).grid(row=row_index, column = col_index)
    col_index += 1

    if col_index > 4 :
        row_index += 1
        col_index = 0

window.mainloop()

'''
from tkinter import*

num = 0
def ac():
    global num
    print(eval())


MyCalculator=Tk()

a = Entry(window)
b = Button(window, text="7", )
b1 = Button(window, text="8", )
b2 = Button(window, text="9", )
b3 = Button(window, text="/", )
b4 = Button(window, text="C", )
b5 = Button(window, text="4", )
b6 = Button(window, text="5", ) 
b7 = Button(window, text="6", )
b8 = Button(window, text="*", )
b9 = Button(window)
b10 = Button(window, text="1", )
b11 = Button(window, text="2", )
b12 = Button(window, text="3", )
b13 = Button(window, text="-", )
b14 = Button(window)
b15 = Button(window, text="0", )
b16 = Button(window, text=".", )
b17 = Button(window, text="=", )
b18 = Button(window, text="+", )
b19 = Button(window)

a.grid(row = 0, column = 0, columnspan = 5)
b.grid(row = 1, column = 0)
b1.grid(row = 1, column = 1)
b2.grid(row = 1, column = 2)
b3.grid(row = 1, column = 3)
b4.grid(row = 1, column = 4)
b5.grid(row = 2, column = 0)
b6.grid(row = 2, column = 1)
b7.grid(row = 2, column = 2)
b8.grid(row = 2, column = 3)
b9.grid(row = 2, column = 4)
b10.grid(row = 3, column = 0)
b11.grid(row = 3, column = 1)
b12.grid(row = 3, column = 2)
b13.grid(row = 3, column = 3)
b14.grid(row = 3, column = 4)
b15.grid(row = 4, column = 0)
b16.grid(row = 4, column = 1)
b17.grid(row = 4, column = 2)
b18.grid(row = 4, column = 3)
b19.grid(row = 4, column = 4)
'''