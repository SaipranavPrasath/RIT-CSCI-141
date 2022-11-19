file name: prefix_search.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele

def open_file(file_name):
    """
    this function opens the file specified by the user.
    :param file_name: the file the user wants to open.
    :return: this makes the items in the file into a list and returns the list.
    """
    fd = open(file_name)
    list1 = []
    for line in fd:
        line = line.strip().lower()
        list1.append(line)
    return list1

def linear_search(list1, prefix):
    """
    this function uses linear search to get the first word starting with the prefix specified by the user.
    :param list1: the list that's being used to find if the specified prefix is in any of the words.
    :param prefix: the prefix specified by the user.
    :return: if one or more words in the list have the prefix specified by the user, the index of the first word with
    the specified prefix is returned. if no words in the list have the prefix specified by the user, -1 is returned
    """
    for index in range(len(list1)):
        if list1[index].startswith(prefix):
            return list1[index]
    return -1

def binary_search(list1, prefix, start, end):
    """
    this function uses binary search to get the first word starting with the prefix specified by the user.
    :param list1: the list that's being used to find if the specified prefix is in any of the words.
    :param prefix: the prefix specified by the user.
    :param start: the start of the list
    :param end: the end of the list, which is the length of the list in this case.
    :return: if the prefix specified by the user is less than the mid-value of the list, the binary search function is
    returned, except 1 is subtracted from the mid-index. if the prefix specified by the user is greater than the
    mid-value of the list, the binary search function is returned, except 1 is added to the mid-index.
    """
    if start > end:
        return None
    mid_index = int((start + end) // 2)
    mid_value = list1[mid_index]
    if mid_value.startswith(prefix):
        return mid_value
    elif prefix < mid_value:
        return binary_search(list1, prefix, 0, mid_index)
    else:
        return binary_search(list1, prefix, mid_index, len(list1) - 1)

def main():
    """
    this function prompts the user for a file name, type of search, and prefix to search for. if the file name isn't one
    of the two available files to be searched, it prints "No file found" and quits. likewise, if the type of search
    isn't either "linear" or "binary, it prints "Invalid search type and quits. while the prefix entered by the user
    isn't an empty string, it prompts the user to enter a prefix to search or a blank line to quit. depending on the
    search type the user inputs, it runs the respective program and outputs the desired results.
    """
    prefix = "temp"
    file_name = input("Enter the name of the file to search: ")
    type_of_search = input("Enter the type of search [ binary / linear ]: ")
    if not (file_name == "word_list.txt" or file_name == "words_sorted.txt"):
        print("No such file found.")
        quit()
    if not (type_of_search == "binary" or type_of_search == "linear"):
        print("Invalid search type.")
        quit()
    while prefix != "":
        prefix = input("Enter a prefix to search or blank line to quit: ")
        if prefix == "":
            print("Thanks for searching!")
            break
        if type_of_search == "binary":
            print(binary_search(open_file(file_name), prefix, 0, len(open_file(file_name))-1))
        elif type_of_search == "linear":
            print(linear_search(open_file(file_name), prefix))

main()
