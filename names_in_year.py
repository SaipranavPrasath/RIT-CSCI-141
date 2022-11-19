file name: names_in_year.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele

import sys  # sys.argv
from dataclasses import dataclass

# The range of valid years of data is 1880 to 2018.
START_YEAR = 1880
END_YEAR = 2018

@dataclass
class YearStats:
    """
    A YearStats structure stores information produced by get_names_in_year().
    Fields:
    year: int; the year that is being looked through
    total: int; the total number of a specific name in that year
    names: dict;
    """
    year: int
    total: int
    names: dict

def get_filename(year):
    """
    get the file path, a string for a filename associated with the year.
    :param year: the desired year
    :return: a string, e.g. './data/yob1990.txt' if year = 1990
    """
    return './data/yob' + str(year) + '.txt'

def get_names_in_year(year):
    """
    For the given year, compute the total number of all names and
    the counts of each individual name but ignoring gender; that is
    combine counts of both genders of a name that is both female and male.
    :param year: the year
    :return: YearStats of year, total names, dictionary mapping names to counts
    """
    get_file_name = get_filename(year)
    names = {}
    total = 0
    fd = open(get_file_name)
    for line in fd:
        line = line.split(",")
        name = line[0]
        count = int(line[2])
        if name in names:
            names[name] += count
        else:
            names[name] = count
        total = total + count
    return YearStats(year, total, names)

def run_query(stats):
    """
    get total names and dictionary of gender insensitive names->count in year,
    and offer a choice to query about any name. 
    If the name is present, print the year, the name,
    the gender-neutral count of occurrences, and the percent of
    the total. If the name is not present, print it is absent,
    Reprompt until the name input is an empty string.
    :param stats: YearStats object
    """

    if stats is None:
        print("Error: no statistics to query")
    else:
        while True:
            name_to_search = input("Enter a name to investigate (return to quit): ")
            if name_to_search == "":
                break
            if name_to_search in stats.names:
                count = stats.names[name_to_search]
                percent = ((count / stats.total) * 100)
                print("year:", stats.year, "\nname:", name_to_search, "\ncount:", count, "\n", str(f'{percent:3.2f}%'),
                      "of all names")
            else:
                print(name_to_search, "is not in the data.")
                continue

def main():
    """
    The main program reads the command line, calls get_names_in_year
    to compute and return the result, and runs a details of the result.
    """
    if len(sys.argv) == 2:
        command_line = sys.argv[1]
    else:
        print("Usage: python3 names_in_year.py year")
    command_line = get_names_in_year(command_line)
    run_query(command_line)

if __name__ == '__main__':
    main()
