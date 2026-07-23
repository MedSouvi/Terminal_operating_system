import turtle
import time


# setup window ======================
window = turtle.Screen()
window.title("Ping Pong Game")
window.setup(width=800, height=600)
window.tracer(0)  # set delay for update drawings
window.bgcolor('black')
window.getcanvas().winfo_toplevel().iconbitmap(r"c:\\Users\\PC\\Downloads\\icons8-python-50.ico")

#textinputloop------------------------------------------------------------
while True:
    player1_name = window.textinput(
            title="player one name",
            prompt="Enter the name of the first player: "
        
        )
    
    player2_name = window.textinput(
            title="player two name", 
            prompt="Enter the name of the second player"
        
        )
    
    if player1_name is None or player2_name is None:
        continue
    
    else:
        if len(player1_name.strip()) >= 4 and len(player2_name.strip()) >= 4:
            break


# setup game objects =================
# ball
ball = turtle.Turtle()
ball.speed(0)  # darwing speed(fastest)
ball.shape("square")
ball.color("white")
# scale factor * default size (20px * 20px)
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.goto(x=0, y=0)  # start position
ball.penup()  # stop drawing lines when moving
ball_dx, ball_dy = 1, 1
ball_speed = 2.5

# center line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
# width => 500px = 25 * 20px default
center_line.shapesize(stretch_len=.1, stretch_wid=25)
center_line.penup()
center_line.goto(0, 0)

# player1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1, stretch_wid=5)
player1.color("blue")
player1.penup()
player1.goto(x=-350, y=0)

# player2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1, stretch_wid=5)
player2.color("red")
player2.penup()
player2.goto(x=350, y=0)

# score text
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(x=0, y=260)
score.write(f"{player1_name}: 0    \\VS\\     {player2_name}: 0", align="center",
                    font=("Courier", 14, "normal"))
score.hideturtle()  # we hide the object because we only want to see the text
p1_score, p2_score = 0, 0  # variables to hold player 1 & player 2 scores

# winer lable
winer_lable = turtle.Turtle()
winer_lable.speed(0)
winer_lable.color("white")
winer_lable.penup()
winer_lable.goto(x=0, y=-280)
winer_lable.hideturtle()


# Players Movement ====================
players_speed = 20


def p1_move_up():
    player1.sety(player1.ycor() + players_speed)


def p1_move_down():
    player1.sety(player1.ycor() - players_speed)


def p2_move_up():
    player2.sety(player2.ycor() + players_speed)


def p2_move_down():
    player2.sety(player2.ycor() - players_speed)


# Get users inputs (Key Bindings)
window.listen()  # tell the window to expect user inputs
window.onkeypress(p1_move_up, "w")  # ensure the keyboard in "En" and "small"
window.onkeypress(p1_move_down, "s")
window.onkeypress(p2_move_up, "Up")
window.onkeypress(p2_move_down, "Down")


def win():
    winner = turtle.Turtle()
    winner.speed(0)
    winner.color("red")
    winner.goto(0, 0)
    winner.penup()   
    winner.hideturtle()
    winner.write(f"congratulations {player1_name if p1_score > p2_score else player2_name}, you are win", 
                 align="center", font=("Courier", 14, "normal")
                )
    

# game mianloop ------------------------------------
while True:
    window.update()

    # ball movement
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))

    # ball & borders collisions
    if(ball.ycor() > 290):   # 290 => 300(top border) - 10(half ball size)
        ball.sety(290)
        ball_dy *= -1  # invert Y direction

    if(ball.ycor() < -290):   # 290 => 300(top border) - 10(half ball size)
        ball.sety(-290)
        ball_dy *= -1  # invert Y direction

    # ball & players collisions =====================
    # collision with player 1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1
        
    # collision with player 2
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (player2.ycor()-60) and ball.ycor() < (player2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1
        
    # score handling
    if(ball.xcor() > 390):
        ball.goto(0, 0)
        ball_dx *= -1  # invert X direction
        score.clear()
        p1_score += 1
        score.write(f"{player1_name}: {p1_score}   \\VS\\    {player2_name}: {p2_score}", align="center",
                    font=("Courier", 14, "normal")
                    )
        
    if(ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1  # invert X direction
        score.clear()
        p2_score += 1
        score.write(f"{player1_name}: {p1_score}   \\VS\\    {player2_name}: {p2_score}", align="center",
                    font=("Courier", 14, "normal")
                    )
                
    if p1_score > p2_score:
        winer_lable.clear()
        winer_lable.write(f"{player1_name}:{p1_score}", align="center", font=("Courier", 14, "normal"))
    else:
        winer_lable.clear()
        winer_lable.write(f"{player2_name}:{p2_score}", align="center", font=("Courier", 14, "normal"))
            
    if abs(p1_score - p2_score) >= 10:
        ball.hideturtle()
        player1.hideturtle()
        player2.hideturtle()
        winer_lable.hideturtle()
        center_line.hideturtle()
        winer_lable.clear()
        center_line.clear()
        score.clear()
        window.bgcolor('green')
        window.title(f" {player1_name if p1_score > p2_score else player2_name} is win")
        window.tracer(0)  
        window.update()
        win()
        window.update()
        print(window.title(f"congratulations {player1_name if p1_score > p2_score else player2_name}, You Win"))
        time.sleep(5)
        break
     
window.bye()