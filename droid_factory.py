file name: droid_factory.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele
  
import cs_queue
from cs_queue import *
from dataclasses import dataclass

@dataclass
class Droid:
    """
    this dataclass contains the parts to build a droid (represented as booleans) as well as each droid's unique, five
    digit serial number (represented as an integer).
    """
    head: bool
    body: bool
    arms: bool
    legs: bool
    serial_number: int

def is_built(droid):
    """
    this function returns true if a droid has been built and false if not.
    :param droid: the droid that is being built.
    :return: the value that is returned depending on what part of the conditional is satisfied.
    """
    if droid.legs == True and droid.arms == True and droid.body == True and droid.head == True:
        return True
    else:
        return False

def open_file(file_name, conveyor_belt):
    """
    this function opens the file inputted by the user, strips each line of white space, and uses the enqueue function to
    add the part onto the conveyor belt, which is a queue.
    :param file_name: the file inputted by the user.
    :param conveyor_belt: the queue that hold the parts.
    """
    fd = open(file_name)
    for line in fd:
        line = line.strip()
        cs_queue.enqueue(conveyor_belt, line)
    fd.close()

def build_a_droid(conveyor_belt, serial_number):
    """
    this function builds a droid. it starts by creating a new droid with no parts and serial number 1000. then, it adds
    whatever parts are missing on a droid onto it until that droid is completed. this continues until either all the
    parts on the conveyor belt are used up or all the droids are completed.
    :param conveyor_belt: the queue that holds the parts.
    :param serial_number: a unique, five-digit number given to every droid.
    """
    print("Building a new droid with serial number", serial_number)
    droid = Droid(False, False, False, False, serial_number)
    while (cs_queue.is_empty(conveyor_belt) == False) and (is_built(droid) == False):
        if droid.arms == False and front(conveyor_belt) == "arms":
            print("attaching arms...")
            droid.arms = True
            cs_queue.dequeue(conveyor_belt)
        elif droid.legs == False and front(conveyor_belt) == "legs":
            print("attaching legs...")
            droid.legs = True
            cs_queue.dequeue(conveyor_belt)
        elif droid.body == False and front(conveyor_belt) == "body":
            print("attaching body...")
            droid.body = True
            cs_queue.dequeue(conveyor_belt)
        elif droid.head == False and front(conveyor_belt) == "head":
            print("attaching head...")
            droid.head = True
            cs_queue.dequeue(conveyor_belt)
        elif droid.arms == False and front(conveyor_belt) != "arms":
            print("placing unneeded part back on belt:", front(conveyor_belt))
            cs_queue.enqueue(conveyor_belt, cs_queue.dequeue(conveyor_belt))
        elif droid.legs == False and front(conveyor_belt) != "legs":
            print("placing unneeded part back on belt:", front(conveyor_belt))
            cs_queue.enqueue(conveyor_belt, cs_queue.dequeue(conveyor_belt))
        elif droid.body == False and front(conveyor_belt) != "body":
            print("placing unneeded part back on belt:", front(conveyor_belt))
            cs_queue.enqueue(conveyor_belt, cs_queue.dequeue(conveyor_belt))
        elif droid.head == False and front(conveyor_belt) != "head":
            print("placing unneeded part back on belt:", front(conveyor_belt))
            cs_queue.enqueue(conveyor_belt, cs_queue.dequeue(conveyor_belt))
    print("Droid", serial_number, "has been assembled!")

def main():
    """
    this function asks the user for a file to input. if the file inputted by the user isn't one of the five available
    files, the program quits. if it is one of the five available files, a queue to hold the parts in the file is created
    and the open_file and build_a_droid functions are executed.
    """
    file_name = input("Enter a parts filename: ")
    print("Starting a shift at the droid factory!")
    if file_name == "droid_parts_0.txt":
        print("All of the droids have been assembled! Time to clock out and play Sabacc...")
    elif file_name == "droid_parts_1.txt" or "droid_parts_3.txt" or "droid_parts_20.txt" or "droid_parts_100.txt":
        conveyor_belt = cs_queue.make_empty_queue()
        open_file(file_name, conveyor_belt)
        i = 10001
        while not is_empty(conveyor_belt):
            build_a_droid(conveyor_belt, i)
            i += 1
        print("All of the droids have been assembled! Time to clock out and play Sabacc...")
    else:
        print("No such file found.")
        quit()

main()
