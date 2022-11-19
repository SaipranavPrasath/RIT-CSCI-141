file name: pentagons.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele

import turtle as tt

def draw_big_pentagon(size):
    """
    :param size: the size, inputted by the user, of one side
    precondition: depth = 1, length > 1
    turtle is facing east
    turtle pen is down
    postcondition: the pentagon was drawn for the current depth
    turtle is facing east
    turtle pen is down
    """
    """
    this function draws the first depth, which is one big pentagon
    """
    tt.fd(size)
    tt.left(72)
    tt.fd(size)
    tt.left(72)
    tt.fd(size)
    tt.left(72)
    tt.fd(size)
    tt.left(72)
    tt.fd(size)
    tt.left(72)

def draw_pentagons_2(size):
    """
    :param size: the size, inputted by the user, of one side
    precondition: depth = 2, length > 1
    turtle is facing east
    turtle pen is down
    postcondition: the pentagons were drawn for the current depth
    turtle is facing east
    turtle pen is down
    """
    """
    this function draws the second depth, which is two pentagons (of half the size as the big pentagon) inside the big
    pentagon
    """
    tt.fd(size)
    tt.left(72)
    tt.fd(size/2)
    draw_big_pentagon(size/2)
    tt.fd(size/2)
    tt.left(72)
    tt.fd(size)
    tt.left(72)
    tt.fd(size/2)
    draw_big_pentagon(size/2)
    tt.fd(size/2)
    tt.left(72)
    tt.fd(size)
    tt.left(72)

def draw_pentagons_3(size):
    """
    :param size: the size, inputted by the user, of one side
    precondition: depth = 3, length > 1
    turtle is facing east
    turtle pen is down
    postcondition: the pentagons were drawn for the current depth
    turtle is facing east
    turtle pen is down
    """
    """
    this function draws the third depth, which is two pentagons (of a third the size as the big pentagon) inside both of
    the pentagons inside the big pentagon
    """
    tt.fd(size)
    tt.left(72)
    tt.fd(size/2)
    draw_pentagons_2(size/2)
    tt.fd(size/2)
    tt.left(72)
    tt.fd(size)
    tt.left(72)
    tt.fd(size/2)
    draw_pentagons_2(size/2)
    tt.fd(size/2)
    tt.left(72)
    tt.fd(size)
    tt.left(72)

def draw_pentagons_rec(size,depth):
    """
    :param size: the size, inputted by the user, of one side
    :param depth: the depth of recursion inputted by the user
    :return: the function is returned if the user inputs a depth less than or equal to 0
    precondition: depth > 3, length > 1
    turtle is facing east
    turtle pen is down
    postcondition: the pentagons were drawn for the chosen depth
    turtle is facing east
    turtle pen is down
    """
    """
    this function is the recursive function that draws any depth greater than 3 and returns the function if the inputted
    depth is less than or equal to 0
    """
    if depth <= 0:
        return
    tt.fd(size)
    tt.left(72)
    tt.fd(size/2)
    draw_pentagons_rec(size/2, depth-1)
    tt.fd(size/2)
    tt.left(72)
    tt.fd(size)
    tt.left(72)
    tt.fd(size/2)
    draw_pentagons_rec(size/2, depth-1)
    tt.fd(size/2)
    tt.left(72)
    tt.fd(size)
    tt.left(72)

def main():
    """
    this function asks the user to input the size of one side and the depth they want. it draws depths 0,1,2,and 3,
    clears the screen after each one, and draws the image up to and including whatever depth the user inputted
    """
    size = int(input("enter a size of 1 side (max 300): "))
    depth = int(input("enter the depth of recursion (min 0): "))
    tt.speed(0)
    draw_pentagons_rec(size, 0)
    input("press enter key to continue")
    tt.clearscreen()
    draw_big_pentagon(size)
    input("press enter key to continue")
    tt.clearscreen()
    draw_pentagons_2(size)
    input("press enter key to continue")
    tt.clearscreen()
    draw_pentagons_3(size)
    input("press enter key to continue")
    tt.clearscreen()
    draw_pentagons_rec(size, depth)
    input("close the canvas window to end the program")
    tt.done()

main()
