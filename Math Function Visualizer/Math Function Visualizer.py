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
        if (y[n].isdigit() and y[n+1].isalpha()) or (y[n+1].isdigit() and y[n].isalpha()) or (y[n]==')' and y[n+1]=='('):#Adding a missing '*' between numbers ,variables and paranthesis for user flexibility
            y=y[:n+1]+'*'+y[n+1:]
            n+=1
        n+=1
    y=y.replace('^','**').replace('sin','math.sin').replace('cos','math.cos').replace('tan','math.tan').replace('e**','(math.e)**').replace('log','math.log').replace('pi','math.pi')
    if 'cosec' in y:
        y=y.replace('math.cosec','cosec')
    for i in ['arcmath.sin','arcmath.cos','arcmath.tan']:
        if i in y:
            y=y.replace(i,'(math.'+i.replace('arcmath.','a')+')')
    if '|' in y:
        if not y.count('|')%2==0:
            print("Invalid input!")
            return
        else:
            open_mod=True
            temp_eqn=''
            for i in range(len(y)):
                if y[i]=='|':
                    if open_mod:
                        temp_eqn+='abs('
                        open_mod=False
                    else:
                        temp_eqn+=')'
                        open_mod=True
                else:
                    temp_eqn+=y[i]
            y=temp_eqn
    x=-400
    x_scale=50
    y_scale=85
    t.penup()
    t.pendown()
    error_count=0
    plotted=False
    while x<=400:#Plotting the points
        try:
            y1=eval(y.replace('x',f'({x})'))
            if not plotted:#Moving to the initial point
                t.penup()
                t.goto(x*x_scale,y1*y_scale)
                plotted=True
                y_temp=y1
                x+=0.1
                t.pendown()
                continue
            if abs((y_temp-y1)/(0.1))>=100:
                t.penup()
            else:
                t.pendown()
            y_temp=y1
            t.goto(x*x_scale,y1*y_scale)
        except:
            error_count+=1
        finally:
            x+=0.1
    if error_count==8000:
        print("Function not defined")
        return
    s.update()
    print(y.replace('math.','').replace('abs','mod'),' has been plotted!')
draw_axis()
s.update()
func=input("Enter the function you would like to graph (Use paranthesis to isolate the contents inside a function): ").strip().lower()
graph(func)
turtle.done()
