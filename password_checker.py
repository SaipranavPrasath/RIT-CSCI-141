file name: password_checker.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele

def length_check(password):
    """
    this function checks to see if the inputted password is at least 10 characters long. if it is, the function returns
    true. if it's not, the function returns false.
    :param password: the password inputted by the user
    :return: the command that terminates the loop/function
    """
    if len(password) >= 10:
        return True
    else:
        return False

def has_digit(password):
    """
    this function checks to see if the inputted password has at least one digit. if it does, the function returns
    true. if it doesn't, the function returns false.
    :param password: the password inputted by the user
    :return: the command that terminates the loop/function
    """
    for digits in password:
        if "0" <= digits <= "9":
            return True
    return False

def has_special(password):
    """
    this function checks to see if the inputted password has at least one special character. if it does, the function
    returns true. if it doesn't, the function returns false.
    :param password: the password inputted by the user
    :return: the command that terminates the loop/function
    """
    special = {"+", "-", "!", "?", "&", "*", "^", "_"}
    for char in special:
        if char in password:
            return True
    return False

def is_not_popular(password):
    """
    this function checks to see if the inputted password is on the rockyou list of popular passwords. if it is, the
    function returns true. if it's not, the function returns false.
    :param password: the password inputted by the user
    :return: the command that terminates the loop/function
    """
    fd = open("rockyou.txt")
    for line in fd:
        line = line.strip()
        if line == password:
            fd.close()
            return False

    fd.close()
    return True

def check_password(password):
    """
    this function runs the above four functions for the boolean value False and prints a corresponding statement to let
    the user know.
    :param password: the password inputted by the user
    """
    if not length_check(password):
        print("Password is too short.")
    if not has_digit(password):
        print("Password doesn't contain a digit.")
    if not has_special(password):
        print("Password doesn't contain a special character: +, -, !, ?, &, *, ^, _")
    if not is_not_popular(password):
        print("Password is often used by other users and not considered secure.")
    elif length_check(password) == True and has_digit(password) == True and has_special(password) == True and is_not_popular(password) == True:
        print("Password is strong.")

def main():
    """
    this function asks the user to input a password and uses a while loop to check said password until it is considered
    strong.
    """
    password = input("Write your password to be checked: ")
    while not password == "":
        check_password(password)
        password = input("Write your password to be checked or press Enter to exit: ")

main()
