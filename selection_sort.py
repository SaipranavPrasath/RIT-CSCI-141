file name: selection_sort.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele
  
def open_file(file_name):
    """
    this function opens the file specified by the user, stores the values in a list, and returns the list
    :param file_name: the file the user wants to open
    :return: the action being done to list1
    """
    fd = open(file_name)
    list1 = []
    for line in fd:
        line = line.strip()
        list1.append(line)
    fd.close()
    return list1

def swap(list1, i, j):
    """
    this function swaps the items of the list at indexes i and j
    :param list1: the list created from the open_file function
    :param i: one of the indexes that's being compared to execute the swap
    :param j: the other index that's being compared to execute the swap
    """
    temp = list1[i]
    list1[i] = list1[j]
    list1[j] = temp

def selection_sort(list1):
    """
    this function sets the min_index as one value and compares each successive item in the list to the one before it.
    if it's less, the min_index becomes the index of the smaller value. if it's not, nothing happens. this continues
    until the list is completely sorted.
    :param list1: the list created from the open_file function
    """
    for i in range(len(list1) - 1):
        min_index = i
        for j in range(i + 1, len(list1)):
            if list1[min_index] > list1[j]:
                min_index = j
        swap(list1, min_index, i)

def insert(lst, mark):
    """
    insert: List(Orderable) NatNum -> None
    Move value at index mark+1 so that it is in its proper place.
    The mark is index of the last value in the sorted part.
    Parameters:
        lst - the list of data
        mark - represents cutting the list between
               index mark and index mark+1
    pre-conditions: lst[0:mark+1] is sorted.
    post-conditions: lst[0:mark+2] is sorted.
    """
    index = mark
    while index > -1 and lst[index] > lst[index + 1]:
        swap(lst, index, index + 1)
        index = index - 1

def insertion_sort(lst):
    """
    insertion_sort : List(Orderable) -> None
    Perform an in-place insertion sort on a list of orderable data.
    Parameters:
        lst - the list of data to sort
    post-conditions:
    The data list is in sorted order.
    """
    for mark in range(len(lst) - 1):
        insert(lst, mark)

l = [91, 17, 18, 29, 42, 10, 95, 73, 96]
insertion_sort(l)
print("Insertion Sort")
print(l)

def main():
    """
    this function prompts the user for a file to search and prints "No such file found" if the file name isn't
    "int-random.txt". then it calls the open_file function which opens the text file, makes the items into a list, and
    prints out the list. after that, it calls the selection_sort function which sorts the items. lastly, the sorted list
    is printed.
    """
    file_name = input("Enter the name of the file to search: ")
    if not (file_name == "int-random.txt"):
        print("No such file found")
        quit()
    lst = open_file(file_name)
    print("Selection Sort")
    print(lst)
    selection_sort(lst)
    print(lst)

main()
