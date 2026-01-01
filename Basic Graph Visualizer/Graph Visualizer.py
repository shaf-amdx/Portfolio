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
        if y[n].isdigit() and y[n+1].isalpha():
            y=y[:n+1]+'*'+y[n+1:]
            n+=1
        n+=1
    y=y.replace('^','**').replace('sin','math.sin').replace('cos','math.cos').replace('tan','math.tan').replace('e**','math.exp').replace('log','math.log').replace('pi','math.pi')
    x=-400
    for i in ['sin','cos','tan','cot','sec','cosec']:
        if i in y:
            x_scale=10
            y_scale=100
            break
    else:
        x_scale=1000
        y_scale=10
    t.penup()
    while True:
        try:
            y1=eval(y.replace('x',f'({x})'))
            t.goto(x*x_scale,y1*y_scale)
        except:
            x+=0.1
        else:
            break
    t.pendown()
    n=0
    while n<800:
        try:
            min_y,max_y=min(eval(y.replace('x',f'({x})')) for x in range(-400+n,401)),max(eval(y.replace('x',f'({x})')) for x in range(-400,401))
        except:
            n+=1
        else:
            break
    y_temp=eval(y.replace('x',f'({x})'))
    while x<=400:
        try:
            y1=eval(y.replace('x',f'({x})'))
            if abs((y_temp-y1)/(0.1))>=30:
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
