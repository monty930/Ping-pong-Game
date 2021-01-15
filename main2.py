import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, -260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Times", 23, "normal"))

pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.goto(350, 260)
pen2.write("exit", align="center", font=("Times", 23, "normal"))


# function
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")

score1 = 0
score2 = 0
exit_check = False


# Main game loop
def f_m():

    global score1
    global score2

    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 350:
        score1 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1, score2), align="center", font=("Times", 23, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score2 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score1, score2), align="center", font=("Times", 23, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -340 and paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50:
        ball.dx *= -1

    def fun(x, y):
        if 380 > x > 320 and 290 > y > 230:
            global exit_check
            exit_check = True

    wn.onclick(fun)


while not exit_check:
    wn.ontimer(f_m(), 10)
