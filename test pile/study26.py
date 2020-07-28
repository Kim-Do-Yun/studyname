import turtle as t
import random

def draw_shape():
    num_list = ['yellow', 'white', 'green', 'blue', 'red', 'orange', 'purple']
    
    for i in range(10):
        x = random.randint(00,300)
        y = random.randint(0,300)
        a = random.randint(3,6)
        #b = random.randint(0,6)
        #c = num_list[b]
        c = random.choice(num_list)
        t.fillcolor(c)
        t.pensize(3)
        t.up()
        t.goto(x,y)
        t.down()
        t.begin_fill()
        for j in range(a):
            t.forward(50)
            t.left(360/a)
        t.end_fill()
    
draw_shape()
t.done()