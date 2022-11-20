file name: schedule.py
author: Saipranav Prasath sp5938@rit.edu
Course: RIT CSCI-141
Section: 3
Professor: Ben Steele

from dataclasses import dataclass

@dataclass
class Projects:
    """
    this dataclass contains the projects and includes three elements: the name of the project, the total length
    (in weeks) of the project, and the revenue generated per week of the project.
    """
    name: str
    length: int
    total_revenue: int

def open_file(file_name):
    """
    this function opens the file inputted by the user and makes it into a list by the three elements, which each
    represent an index.
    :param file_name: the file inputted by the user
    :return: the list that is returned with the different available projects.
    """
    list1 = []
    name = 0
    length = 1
    total_revenue = 2
    fd = open(file_name)
    for line in fd:
        line = line.split(" ")
        project = Projects(line[name], int(line[length]), int(line[total_revenue]))
        list1.append(project)
    return list1

def insertion_sort(projects):
    """
    this function performs insertion sort on the list of available projects.
    :param projects: the options of projects to complete
    :return: the list that is returned with the projects sorted by revenue generated per week.
    """
    for index in range(1, len(projects)):
        target_project = projects[index]
        revenue_per_week = target_project.total_revenue / target_project.length
        j = index
        while j > 0 and (revenue_per_week > (projects[j - 1].total_revenue / projects[j - 1].length)):
            projects[j] = projects[j - 1]
            j = j - 1
        projects[j] = target_project
    return projects

def get_best_project(weeks_limit, sorted_projects):
    """
    this function uses an accumulator to get the best projects to complete from the list of available projects.
    :param weeks_limit: the number of weeks given to generate the most revenue.
    :param sorted_projects: the list of sorted projects by the best projects to complete in the given time period.
    :return: the list that is returned with the best projects to complete in the given time period.
    """
    best_projects = []
    accumulator = 0
    for project in sorted_projects:
        if accumulator + project.length <= weeks_limit:
            best_projects.append(project)
            accumulator += project.length
    return best_projects

def get_total_revenue(best_project):
    """
    this function calculates the total revenue generated from the list of completed projects.
    :param best_project: the list of best projects to complete in the given time period.
    :return: the total revenue generated from completing the best projects.
    """
    accumulator = 0
    for index in best_project:
        accumulator += index.total_revenue
    return accumulator

def weeks_remaining(best_project, weeks_limit):
    """
    this function calculate the amount of remaining weeks to make sure more time than is given isn't taken.
    :param best_project: the list of best projects to complete in the given time period.
    :param weeks_limit: the given time period.
    :return: the number of weeks remaining after every project in the list of best projects is completed.
    """
    accumulator = 0
    for index in best_project:
        accumulator += index.length
    return weeks_limit - accumulator

def print_projects(projects):
    """
    this function prints everything vertically as shown in the writeup instead of horizontally.
    :param projects: the list of projects
    """
    for i in projects:
        print(i.name, i.length, i.total_revenue)

def main():
    """
    this function asks the user to input a file name and the number of weeks and runs all the functions above to produce
    the output given in the writeup.
    """
    file_name = input("Please enter a file name: ")
    weeks_limit = int(input("Enter the length of the period (weeks): "))
    if file_name == "file1.txt" or "file2.txt" or "projects.txt":
        list2 = open_file(file_name)
        print("\ninitial projects\n")
        print_projects(list2)
        proj = insertion_sort(list2)
        print("\nprojects organized by rev/week\n")
        print_projects(proj)
        best_project = get_best_project(weeks_limit, proj)
        print("\nschedule\n")
        print_projects(best_project)
        total = get_total_revenue(best_project)
        print("\nTotal revenue: $", total)
        weeks = weeks_remaining(best_project, weeks_limit)
        print("\nUnscheduled weeks:", weeks)
    else:
        print("No such file found.")
        quit()

main()
