import sys
sys.path.append("/usr/local/lib/python3.8/site-packages")
import turtle

def create_base_mat(x):
    turtle.pu()
    turtle.setpos((x*54)/-2,(x*78)/-2)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.fd(x*54)
    turtle.left(90)
    turtle.fd(x*78)
    turtle.left(90)
    turtle.fd(x*54)
    turtle.left(90)
    turtle.fd(x*78)
    turtle.left(90)
    turtle.pu()


def u(x):
    turtle.pu()
    turtle.setpos((x*54)/-2,(x*78)/-2)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.fd(x*54)
    turtle.left(90)
    turtle.fd(x*78)
    turtle.left(90)
    turtle.fd(x*54)
    turtle.left(90)
    turtle.fd(x*78)
    turtle.left(90)
    turtle.pu()

create_base_mat(8)
print("test")
