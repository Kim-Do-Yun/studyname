import turtle as t

def f(x) :
    return (x*x + 1) * 0.01

t.forward(100)
t.backward(100)
t.left(90)
t.forward(100)
t.backward(100)

for x in range(0,100):
    t.goto(x,f(x))

t.done()