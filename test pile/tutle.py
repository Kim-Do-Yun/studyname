import turtle as t
t.shape("turtle")

def square() :
    for _ in range(4) :
        t.forward(100)
        t.left(90)

for i in range(3) :
    t.up()
    t.goto(i*150, 0)
    t.down()
    square()

t.done()