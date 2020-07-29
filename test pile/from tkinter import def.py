from tkinter import*


def haha():
    df = int(c.get())*2.54
    e["text"] = str(df) + "센티미터"


window = Tk()
a = Label(window, text="인치를 센티미터로 변환하는 프로그램")
b = Label(window, text="인치를 입력하시오:")
c = Entry(window)
d = Label(window, text="변환결과:")
e = Label(window, text="결과값이 출력됩니다.")
f = Button(window, text="변환", command = haha)
a.grid(row = 0, column = 0, columnspan = 2)
b.grid(row = 1, column = 0)
c.grid(row = 1, column = 1)
d.grid(row = 2, column = 0)
e.grid(row = 2, column = 1)
f.grid(row = 3, column = 1)

window.mainloop()