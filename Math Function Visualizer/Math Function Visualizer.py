import turtle
import math
s=turtle.Screen()
s.tracer(0,0)
t=turtle.Turtle()
s.bgcolor('black')
t.pencolor('white')
t.speed(0)
t.hideturtle()
def draw_axis():#Drawing the x and y axis
    t.forward(1000)
    t.home()
    t.backward(1000)
    t.home()
    t.right(90)
    t.forward(1000)
    t.home()
    t.right(90)
    t.backward(1000)
def cosec(x):
    return 1/(math.sin(x))
def sec(x):
    return 1/(math.cos(x))
def cot(x):
    return 1/(math.tan(x))
def graph(y):
    t.home()
    n=0
    while n<len(y)-1:
        if (y[n].isdigit() and y[n+1].isalpha()) or (y[n+1].isdigit() and y[n].isalpha()) or ((y[n].isdigit() or y[n].isalpha()) and y[n+1]=='('):#Adding a missing '*' between numbers ,variables and paranthesis
            y=y[:n+1]+'*'+y[n+1:]
            n+=1
        n+=1
    y=y.replace('^','**').replace('sin','math.sin').replace('cos','math.cos').replace('tan','math.tan').replace('e**','math.exp').replace('log','math.log').replace('pi','math.pi')
    x=-400
    for i in ['sin','cos','tan','cot','sec','cosec']:#Setting scale for specific functions
        if i in y:
            x_scale=10
            y_scale=100
            break
    else:
        x_scale=1000
        y_scale=10
    t.penup()
    while True:#Moving to the initial point
        try:
            y1=eval(y.replace('x',f'({x})'))
            t.goto(x*x_scale,y1*y_scale)
        except:
            x+=0.1
        else:
            break
    t.pendown()
    y_temp=eval(y.replace('x',f'({x})'))
    while x<=400:#Plotting the points
        try:
            y1=eval(y.replace('x',f'({x})'))
            if abs((y_temp-y1)/(0.1))>=50:
                t.penup()
            else:
                t.pendown()
            y_temp=y1
            t.goto(x*10,y1*100)
        except:
            pass
        finally:
            x+=0.1
    s.update()
    print(y.replace('math.',''),' has been plotted!')
draw_axis()
s.update()
func=input("Enter the function you would like to graph : ").strip().lower()
graph(func)
turtle.done()
