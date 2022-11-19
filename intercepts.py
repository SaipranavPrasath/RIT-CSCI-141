file name: intercepts.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele

def no_x_intercept(m, b):
    """
    m represents the slope of the line and b represents the y int of the line
    the function returns true or false depending on the conditions in which there would be no x int
    """
    if m == 0 and b != 0:
        return True
    else:
        return False

def x_intercept(m, b):
    """
    m represents the slope of the line and b represents the y int of the line
    the function returns the value (if any) of the x int
    """
    if no_x_intercept(m, b):
        return None
    elif m == 0:
        return 0
    else:
        return -b / m

def y_intercept(m, b):
    """
    the function returns the y int
    """
    return b

def print_point(x, y):
    """
    the function prints the point, (x, y), formatted to three decimal places
    """
    if x is None:
        print("(NONE)", end=" ")
    else:
        print("(", format(x, ".3f"), ", ", format(y, ".3f"), ")", sep="", end=" ")

def test_case(m, b):
    """
    the function prints the equation and intercepts of the test case ordered pairs
    """
    print("Equation: Y = ", m, " X + ", b, ". Intercepts: ", end="", sep="")
    print_point(x_intercept(m, b), 0)
    print_point(0, y_intercept(m, b))
    print()

def main():
    test_case(0, 5)
    test_case(-2, 0)
    test_case(-1, 1)
    test_case(4, -4)
    test_case(3, 6)
    test_case(5, -3)
    test_case(-10, 2)
    test_case(1, -1)
    test_case(0, 4)
    test_case(3, 3)

main()
