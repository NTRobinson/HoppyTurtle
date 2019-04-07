# Blindsey - main loop
import os
import time
import turtle
import random

# set up the screen (1000 X 1000 pixels in size)
main_screen = turtle.Screen()
main_screen.bgcolor("cyan")
main_screen.title("BLINDSEY")

main_screen.bgpic("background.gif")

# create player turtle
player = turtle.Turtle()
player.color("black")
player.shape("circle")
player.penup()
player.speed(0)
player.setposition(-400, 0)

player_speed = 100

# create first set of pillars
pillar = turtle.Turtle()
pillar.hideturtle()
pillar_upper = turtle.Turtle()
pillar_upper.hideturtle()
pillar.color("purple")
pillar_upper.color("purple")
pillar.shape("square")
pillar_upper.shape("square")
pillar.shapesize(35, 2)
pillar_upper.shapesize(35,2)
pillar.penup()
pillar_upper.penup()
pillar.speed(0)
pillar_upper.speed(0)
pillar.setposition(400, -500)
pillar.showturtle()
pillar_upper.setposition(600, 500)
pillar_upper.showturtle()

# create second set of pillars
pillar2 = turtle.Turtle()
pillar2.hideturtle()
pillar_upper2 = turtle.Turtle()
pillar_upper2.hideturtle()
pillar2.color("purple")
pillar_upper2.color("purple")
pillar2.shape("square")
pillar_upper2.shape("square")
pillar2.shapesize(35, 2)
pillar_upper2.shapesize(35,2)
pillar2.penup()
pillar_upper2.penup()
pillar2.speed(0)
pillar_upper2.speed(0)
pillar2.setposition(800, -500)
pillar2.showturtle()
pillar_upper2.setposition(1000, 500)
pillar_upper2.showturtle()

pillar_speed = 50


def update_objects():
    player.sety(player.ycor() - 10)
    pillar.setx(pillar.xcor() - pillar_speed)
    pillar_upper.setx(pillar_upper.xcor() - pillar_speed)

    pillar2.setx(pillar2.xcor() - pillar_speed)
    pillar_upper2.setx(pillar_upper2.xcor() - pillar_speed)

    if pillar.xcor() < -500 :
        pillar.setx(500)
        pillar.shapesize(25 + random.randrange(0, 25), 2)

    if pillar_upper.xcor() < -500 :
        pillar_upper.setx(500)
        pillar_upper.shapesize(30 + random.randrange(0, 20), 2)

    if pillar2.xcor() < -500 :
        pillar2.setx(500)
        pillar2.shapesize(25 + random.randrange(0, 25), 2)

    if pillar_upper2.xcor() < -500 :
        pillar_upper2.setx(500)
        pillar_upper2.shapesize(30 + random.randrange(0, 20), 2)

# move player up
def mov_up():
    y = player.ycor()
    y = y + player_speed
    player.sety(y)

main_screen.textinput("Are you ready?", "Press OK to continue...")

score = 0

# main loop
while True:
    # keyboard input
    turtle.listen()
    turtle.onkey(mov_up, "Up")

    # loose on contact at y = -300
    if player.ycor() > -300 :
        update_objects()

        pillar_coords = pillar.get_shapepoly()
        pillar_top_y = pillar_coords[0][0] - 500

        pillar_upper_coords = pillar_upper.get_shapepoly()
        pillar_upper_bottom_y = 500 - pillar_upper_coords[0][0]

        pillar_coords2 = pillar2.get_shapepoly()
        pillar_top_y2 = pillar_coords2[0][0] - 500

        pillar_upper_coords2 = pillar_upper2.get_shapepoly()
        pillar_upper_bottom_y2 = 500 - pillar_upper_coords2[0][0]

        if player.xcor() == pillar.xcor() :
            if player.ycor() < pillar_top_y :
                print('Oops. You hit a pillar!!')
                break

        if player.xcor() == pillar_upper.xcor() :
            if player.ycor() > pillar_upper_bottom_y :
                print('Oops. You hit a pillar!!')
                break

        if player.xcor() == pillar2.xcor() :
            if player.ycor() < pillar_top_y2 :
                print('Oops. You hit a pillar!!')
                break

        if player.xcor() == pillar_upper2.xcor() :
            if player.ycor() > pillar_upper_bottom_y2 :
                print('Oops. You hit a pillar!!')
                break
        score = score + 1
    else :
        print('You hit the ground...')
        break

print("Your score is: ", score)