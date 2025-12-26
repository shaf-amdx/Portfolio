def draw_graph(func):
    t.home()
    for i in range(3000):
        try:
            if func=="sinx":
                y=math.sin(i)*40
                x=i*5
            elif func=="cosx":
                y=math.cos(i)*40
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
            if func=="e**x":
                y=math.exp(i)
                x=i*100
            elif "**" in func:
                y=int(func.split("**")[0])**i
                x=i*10
            else:
                print("Sorry We have not yet developed the program inorder to evaluate ur function!")
        except ZeroDivisionError:
            continue
        t.goto(x,y)
func=input("Enter the function you would like to graph : ").strip().lower()
import turtle
import math
s=turtle.Screen()
t=turtle.Turtle()
s.bgcolor('black')
t.pencolor('white')
t.speed(70)
t.hideturtle()
#Drawing the x and y axis
t.forward(1000)
t.home()
t.backward(1000)
t.home()
t.right(90)
t.forward(1000)
t.home()
t.right(90)
t.backward(1000)
draw_graph(func)
t.done()
