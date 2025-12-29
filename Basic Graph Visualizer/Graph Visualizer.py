def draw_graph(func):
    t.home()
    for i in range(3000):
        try:
            if func=="sinx":
                y=math.sin(i)*50
                x=i*5
            elif func=="cosx":
                y=math.cos(i)*50
                x=i*5
            elif func=="tanx":
                y=100*(math.sin(i)/math.cos(i))
                x=i
            elif func=="cotx":
                y=100*(math.cos(i)/math.sin(i))
                x=i
            elif func=="secx":
                y=(100/(math.cos(math.radians(i))))
                x=i
            elif func=="cosecx":
                y=(100/(math.sin(math.radians(i))))
                x=i
            elif func=="e**x":
                y=math.exp(i)
                x=i*100
            elif "**" in func:
                y=int(func.split("**")[0])**i
                x=i*10
            else:
                print("Sorry We have not yet developed the program inorder to evaluate ur function (Note: Type 'polynomial' for plotting a polynomial first)!")
        except ZeroDivisionError:
            continue
        t.goto(x,y)
    s.update()
def polynomial_graph(y):
    y=y.replace('^','**')
    n=0
    while n<len(y)-1:
        if y[n].isdigit() and y[n+1].isalpha():
            y=y[:n+1]+'*'+y[n+1:]
            n+=1
        n+=1
    x=-400
    t.penup()
    print(y)
    while True:
        y1=eval(y.replace('x',f'({x})'))
        try:
            t.goto(x,y1)
        except:
            x+=1
        else:
            break
    t.pendown()
    while x<=400:
        try:
            t.goto(x,eval(y.replace('x',f'({x})'))/100)
        except:
            pass
        finally:
            x+=1
    s.update()
func=input("Enter the function you would like to graph (enter 'polynomial' for plotting a polynomial): ").strip().lower()
import turtle
import math
s=turtle.Screen()
s.tracer(0,0)
t=turtle.Turtle()
s.bgcolor('black')
t.pencolor('white')
t.speed(0)
t.hideturtle()
#Drawing the x and y axis
def draw_axis():
    t.forward(1000)
    t.home()
    t.backward(1000)
    t.home()
    t.right(90)
    t.forward(1000)
    t.home()
    t.right(90)
    t.backward(1000)
draw_axis()
s.update()
if func=='polynomial':
    y=input("Enter ur expression in terms of x : ")
    polynomial_graph(y)
else:
    draw_graph(func)
turtle.done()
