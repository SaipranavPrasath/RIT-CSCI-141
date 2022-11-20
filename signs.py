file name: signs.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele
  
import turtle as tt

def shape():
    """
    shape draws the rhombus which can be used to create all four signs
    """
    tt.penup()
    tt.back(200)
    tt.fd(100)
    tt.pendown()
    tt.pencolor("black")
    tt.pensize(5)
    tt.fillcolor("yellow")
    tt.begin_fill()
    tt.left(135)
    tt.fd(80)
    tt.left(90)
    tt.fd(80)
    tt.left(90)
    tt.fd(80)
    tt.left(90)
    tt.fd(80)
    tt.end_fill()

def inside1():
    """
    inside1 draws the inside of the first sign
    """
    tt.left(135)
    tt.pencolor("black")
    tt.pensize(10)
    tt.penup()
    tt.fd(60)
    tt.pendown()
    tt.right(90)
    tt.penup()
    tt.back(25)
    tt.pendown()
    tt.fd(60)
    tt.back(30)
    tt.right(90)
    tt.fd(30)

def sign1():
    """
    sign1 draws the first sign
    """
    shape()
    inside1()

sign1()
tt.penup()
tt.fd(100)
tt.pendown()

def inside2():
    """
    inside2 draws the inside of the second sign
    """
    tt.left(135)
    tt.pencolor("black")
    tt.pensize(10)
    tt.penup()
    tt.fd(60)
    tt.pendown()
    tt.left(90)
    tt.penup()
    tt.back(25)
    tt.pendown()
    tt.back(10)
    tt.fd(65)
    tt.back(35)
    tt.right(90)
    tt.fd(30)

def sign2():
    """
    sign2 draws the second sign
    """
    tt.penup()
    tt.fd(150)
    shape()
    inside2()

sign2()
tt.penup()
tt.fd(100)
tt.pendown()

def inside3():
    """
    inside3 draws the inside of the third sign
    """
    tt.left(135)
    tt.pencolor("black")
    tt.pensize(10)
    tt.penup()
    tt.fd(60)
    tt.pendown()
    tt.left(90)
    tt.penup()
    tt.back(25)
    tt.pendown()
    tt.back(10)
    tt.fd(60)
    tt.right(90)
    tt.fd(20)
    tt.back(45)

def sign3():
    """
    sign3 draws the third sign
    """
    tt.penup()
    tt.back(100)
    shape()
    inside3()

sign3()
tt.penup()
tt.right(90)
tt.fd(28)
tt.left(90)
tt.pendown()

def inside4():
    """
    our_sign draws the inside of the sign we created
    """
    tt.penup()
    tt.pencolor("yellow")
    tt.fillcolor("black")
    tt.begin_fill()
    tt.left(-25)
    tt.back(50)
    tt.circle(25)
    tt.end_fill()

def sign4():
    """
    sign4 draws the sign we created
    """
    tt.penup()
    tt.fd(300)
    tt.pendown()
    shape()
    inside4()

sign4()
tt.done()
