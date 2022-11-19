file name: fruitful_fun.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele

def sum_squares(n):
    """
    this function is the non-tail recursive version of the sum_squares function. if the value of n is 0 it returns 0,
    otherwise it returns the square of n plus the value of the function after decreasing n by one (so it eventually satisfies the
    base case and the program terminates)
    :param n: a number 1-6
    :return: the value that is returned if the else part of the conditional statement is satisfied
    """
    if n == 0:
        return 0
    else:
        return n*n + (sum_squares(n-1))

def sum_squares_accum(n, accum = 0):
    """
    this function is the tail recursive version of the sum_squares function, therefore it does exactly what that
    function does
    :param n: a number 1-6
    :param accum: the accumulator, which increases as the value of n increases. it is then added to the value of n
    squared if n > 0
    :return: the value that is returned if the else part of the conditional statement is satisfied
    """
    if n == 0:
        return accum
    else:
        return sum_squares_accum(n-1, n*n + accum)

def sum_squares_tail(n):
    """
    this function simply returns the value of sum_squares_accum
    :param n: a number 1-6
    :return: the value that is returned when the function is called
    """
    return sum_squares_accum(n)

def sum_squares_test():
    """
    this function includes test cases to see if the program runs correctly
    """
    print("")
    print("Sum of Squares Test")
    print("n = 0: ", sum_squares(0), sum_squares_tail(0))
    print("n = 1: ", sum_squares(1), sum_squares_tail(1))
    print("n = 2: ", sum_squares(2), sum_squares_tail(2))
    print("n = 3: ", sum_squares(3), sum_squares_tail(3))
    print("n = 4: ", sum_squares(4), sum_squares_tail(4))
    print("n = 5: ", sum_squares(5), sum_squares_tail(5))
    print("n = 6: ", sum_squares(6), sum_squares_tail(6))

def stair_climb(n):
    """
    this function returns a value if n = 1, 2, or 3 and calculates the value using an equation if n > 3
    :param n: a number 1-3, because you can climb 1, 2, or 3 stairs at once
    :return: the value that is returned if a certain condition is satisfied
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n > 3:
        return stair_climb(n-1) + stair_climb(n-2) + stair_climb(n-3)

def stair_climb_accum(n, accum1=1, accum2=2, accum3=4):
    """
    :param n: a number 1-6
    :param accum1: accumulator 1
    :param accum2: accumulator 2
    :param accum3: accumulator 3
    :return:the value that is returned if a certain condition is satisfied
    """
    if n == 1:
        return accum1
    elif n == 2:
        return accum2
    elif n == 3:
        return accum3
    else:
        total = accum1 + accum2 + accum3
        return stair_climb_accum(n-1, accum2, accum3, total)

def stair_climb_tail(n):
    """
    this function simply returns the value of stair_climb_accum
    :param n: a number 1-6
    :return: the value that is returned when the function is called
    """
    return stair_climb_accum(n)

def stair_climb_test():
    """
    this function includes test cases to see if the program works correctly
    """
    print("Sum of Stairs Test")
    print("n = 1: ", stair_climb(1), stair_climb_tail(1))
    print("n = 2: ", stair_climb(2), stair_climb_tail(2))
    print("n = 3: ", stair_climb(3), stair_climb_tail(3))
    print("n = 4: ", stair_climb(4), stair_climb_tail(4))
    print("n = 5: ", stair_climb(5), stair_climb_tail(5))
    print("n = 6: ", stair_climb(6), stair_climb_tail(6))

def main():
    """
    this function executes the above two programs with a space in the middle
    """
    sum_squares_test()
    print("")
    stair_climb_test()

main()
