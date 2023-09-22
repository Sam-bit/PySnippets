import turtle as t
import time

def initdata():
    t.setup(800,600)
    t.pencolor('red')
    t.pensize(5)
    t.speed(10)

def move_pen(x,y):
    t.hideturtle()
    t.up()
    t.goto(x,y)
    t.down()
    t.showturtle()

def hart_arc():
    for i in range(200):
        t.right(1)
        t.forward(2)

def draw():
    
    initdata()
    move_pen(0,-180)
    t.left(140) 
    t.fillcolor("pink")
    t.begin_fill()  
    t.forward(224)  
    hart_arc() 
    t.left(120) 
    hart_arc() 
    t.forward(224)
    t.end_fill()  
    move_pen(x=70, y=160) 
    t.left(185) 
    t.circle(-110,185)  
    t.forward(50)
    move_pen(-180,-180)
    t.left(180) 
    t.forward(600)  
    move_pen(0,50)
    t.hideturtle() 
    t.color('#CD5C5C', 'red')  
    t.write('I Love You,\nABHIPSHA', font=('Arial', 20, 'bold'), align="center")
    t.color('red', 'pink')
    time.sleep(2)
    move_pen(220, -180)
    t.hideturtle()
    
def main():
    draw()
    time.sleep(5)
if __name__ == '__main__':
    main()