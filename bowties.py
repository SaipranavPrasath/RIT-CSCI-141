file name: bowties.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele

import turtle as tt

def init():
    """
    sets up a square drawing canvas 720*720 units
    initializes the turtle's pen size
    """
    tt.setup(720, 720)
    tt.up()
    tt.pensize(5)

def draw_one_bowtie(size):
    """
    this function draws one bowtie with side length 'size' and a circle in the middle with radius 'size/4'
    the outline of the bowtie is blue and the circle is filled in red
    precondition: turtle is facing east, turtle pen is up
    postcondition: turtle is facing east, turtle pen is up
    """
    tt.pencolor("blue")
    tt.left(30)
    tt.fd(size)
    tt.right(120)
    tt.fd(size)
    tt.right(120)
    tt.fd(2 * size)
    tt.left(120)
    tt.fd(size)
    tt.left(120)
    tt.fd(size)
    tt.left(330)
    tt.right(90)
    tt.penup()
    tt.fd(size / 4)
    tt.left(90)
    tt.fillcolor("red")
    tt.begin_fill()
    tt.down()
    tt.circle(size / 4)
    tt.end_fill()
    tt.up()
    tt.right(90)
    tt.back(size / 4)
    tt.left(90)

def draw_bowties_rec(size, depth):
    """
    the function draws the desired figure with the largest bowtie having side length 'size' and the bowties in each
    successive level decreasing by a factor of 3
    the circle's radius is 1/4 the size of one of the sides of the triangle
    precondition: turtle is at the origin, facing east, turtle pen is up
    postcondition: turtle is at the origin, facing east, turtle pen is up
    """
    if depth == 0:
        pass
    else:
        draw_one_bowtie(size)
        if depth > 1:
            tt.up()
            tt.right(30)
            tt.back(2 * size)
            tt.down()
            draw_bowties_rec(size / 3, depth - 1)
            tt.up()
            tt.fd(4 * size)
            tt.down()
            draw_bowties_rec(size / 3, depth - 1)
            tt.up()
            tt.back(2 * size)
            tt.left(60)
            tt.fd(2 * size)
            tt.down()
            draw_bowties_rec(size / 3, depth - 1)
            tt.up()
            tt.back(4 * size)
            tt.down()
            draw_bowties_rec(size / 3, depth - 1)
            tt.up()
            tt.fd(2 * size)
            tt.right(30)

def main():
    """
    sets up a square drawing canvas, prompts for size and depth of recursion, and draw the corresponding image
    """
    size = int(input("enter a size: "))
    depth = int(input("enter a depth: "))
    tt.speed(0)
    draw_bowties_rec(size, depth)
    tt.done()
    
main()
