	#PArt 1
#settting up screen
#2.7
import turtle
import os
#screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('space')


# border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#create player
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#create enemy
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)

enemyspeed = 2

#create the bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(.2,.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready- ready to fire
#fire- bullert fireing
bulletstate = "ready"

#move player
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
    #Declare bullletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #move the bullet to the justa above the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()



# keyboard bindings
turtle.listen()
turtle.onkey(move_left, 'Left')
turtle.onkey(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')

#main game loop
while True:
    #move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    #move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *=  -1
        enemy.sety(y)

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1
        enemy.sety(y)

    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check to see if bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"




















delay = input("Press enter to finish.")
