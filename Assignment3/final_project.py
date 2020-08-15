"""
File: final_project.py
----------------
This is an improved calendar where you can have a different views.
It will update the view when you command your request in the console
"""

import tkinter
import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from datetime import *

CANVAS_WIDTH = 500  # Width of drawing canvas in pixels
CANVAS_HEIGHT = 500  # Height of drawing canvas in pixels
SQUARE_SIZE = 70
NUM_MONTHS = 12
NUM_DAYS_IN_WEEK = 7
LINE_GAP = 20
WIDTH_GAP = 95
FONT = "Calibri 12"


def is_leap_year(year):
    """
    Returns Boolean indicating if given year is a leap year.
    It is a leap year if the year is:
    * divisible by 4, but not divisible by 100
     OR
    * divisible by 400
    (Example of a "predicate function")

    Doctests:
    >>> is_leap_year(2001)
    False
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(1900)
    False
    """
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


def days_in_month(month, year):
    """
    Returns the number of days in the given month and year.
    Assumes that month 1 is January, month 2 is February, and so on.

    Doctests:
    >>> days_in_month(4, 2020)
    30
    >>> days_in_month(2, 1900)
    28
    """
    # Days in February depends on whether it's a leap year
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    # April, June, September, November have 30 days
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    # All other months have 31 days
    else:
        return 31


def print_month_header(month, canvas):
    """
    Prints header for a given month in the calendar
    """
    mydate = datetime.now()
    month_name = date(mydate.year, month, 1).strftime('%B')
    canvas.create_text(10, LINE_GAP * 5, fill="black", font=FONT, text= "Month #" + str(month) + " " + month_name, anchor="nw", tag="monthly_display_object")
    canvas.create_text(10, LINE_GAP * 6, fill="black", font="Times 10", text= "Sun Mon Tue Wed Thu Fri Sat", anchor="nw", tag="monthly_display_object")



def print_month(canvas, month):
    """
    Prints a daily calendar for the given month and year.
    """
    today = date.today()
    year = today.year
    first_day = first_day_of_month(month,year)
    print_month_header(month, canvas)
    days = days_in_month(month, year)
    weekly_gap = 10
    row_number = 7
    # creating gap by leading space before the first day in this month
    for i in range(first_day):
        weekly_gap += 26  # 10 pixel per day

    # Print numbers for all the days in the month
    for i in range(0, days):
        if i < 10:
            str_space = " "
        else:
            str_space = ""
        # changing fill color for today
        if i + 1 == today.day and month == today.month:
            color = "blue"
        else:
            color = "black"
        canvas.create_text(weekly_gap, LINE_GAP * row_number, fill= color, font="Times 10", text=str_space + str(i + 1), anchor="nw", tag="monthly_display_object")
        # Add a new line at end of the week
        weekly_gap += 26
        if ((first_day + i) % NUM_DAYS_IN_WEEK) == (NUM_DAYS_IN_WEEK - 1):
            row_number += 1
            weekly_gap = 10


def print_week(canvas):
    """
    Prints a daily calendar for the current week.
    """
    today = date.today()
    month = today.month
    year = today.year
    first_day = first_day_of_month(month,year)
    print_month_header(month, canvas)
    days = days_in_month(month, year)
    weekly_gap = 10
    row_number = 7
    week = 1
    # creating gap by leading space before the first day in this month
    for i in range(first_day):
        weekly_gap += 26  # 26 pixel per day

    # Print numbers for all the days in the month
    for i in range(0, days):
        # adding gap for single numbers
        if i < 10:
            str_space = " "
        else:
            str_space = ""
        # changing fill color for today
        if i + 1 == today.day:
            color = "blue"
        else:
            color = "black"
        canvas.create_text(weekly_gap, LINE_GAP * row_number, fill=color, font="Times 10", text=str_space + str(i + 1), anchor="nw", tag="week_" + str(week))
        # Add a new line at end of the week
        weekly_gap += 26
        if ((first_day + i) % NUM_DAYS_IN_WEEK) == (NUM_DAYS_IN_WEEK - 1):
            week += 1
            weekly_gap = 10
    for i in range(1, 7):
        if (today.day + first_day) // NUM_DAYS_IN_WEEK + 1 != i:
            canvas.delete("week_" + str(i))


def first_day_of_month(month, year):
    # return the first day of the month
    first_day = first_day_of_year(year)
    for i in range(1, month):
        days = days_in_month(i, year)
        first_day = (first_day + days) % NUM_DAYS_IN_WEEK
    return first_day


def first_day_of_year(year):
    """
    Returns the first day of the week for a given year, where
    (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
    The formula in this function comes from http://mathforum.org/
    >>> first_day_of_year(2020)
    3
    """
    year -= 1
    return (year + (year // 4) - (year // 100) + (year // 400) + 1) % NUM_DAYS_IN_WEEK


def click_event(event):
    x = event.x
    y = event.y
    # events based on location pressed
    if LINE_GAP * 3 < y < LINE_GAP * 4 and 10 < x < 105:
        # click on "weekly display"
        # deleting month items and calling print_week function to present the week
        event.widget.delete("monthly_display_object")
        print_week(event.widget)
    elif LINE_GAP * 4 < y < LINE_GAP * 5 and 10 < x < 105:
        # click on "monthly display"
        dis_month = display_month(0)
        # deleting week items and calling print_month function to present the week
        for i in range(1, 6):
            event.widget.delete("week_" + str(i))
        event.widget.delete("monthly_display_object")
        print_month(event.widget, dis_month)
    elif LINE_GAP * 4 < y < LINE_GAP * 5 and 20 + WIDTH_GAP * 1 < x < 10 + WIDTH_GAP * 2:
        # click on "next month"
        # adding a month to the month display
        dis_month = display_month(1)
        # deleting week items and calling print_month function to present the week
        for i in range(1, 6):
            event.widget.delete("week_" + str(i))
        event.widget.delete("monthly_display_object")
        print_month(event.widget, dis_month)
    elif LINE_GAP * 4 < y < LINE_GAP * 5 and 10 + WIDTH_GAP * 2 < x < 20 + WIDTH_GAP * 3:
        # click on "Previous month"
        dis_month = display_month(-1)
        # deleting week items and calling print_month function to present the week
        for i in range(1, 6):
            event.widget.delete("week_" + str(i))
        event.widget.delete("monthly_display_object")
        print_month(event.widget, dis_month)
    elif LINE_GAP * 15 < y < LINE_GAP * 15 + 25 and 10 < x < 125:
        # click on "Add a meeting"
        add_meeting(event.widget)
    elif LINE_GAP * 15 < y < LINE_GAP * 15 + 25 and 125 + 10 < x < 125 * 2 + 5:
        # click on "Delete a meeting"
        delete_meeting(event.widget)


def display_month(dm):
    # create a fake global variable to change the displayed month
    with open('dummyf.txt','r') as file:
        bla1 = file.readline().split()
        dummy2 = ''
        for i in range (len(bla1)):
            dummy2 += bla1[i]
        dummy2 = int(dummy2) + dm
        if dummy2 == 13:
            dummy2 = 1
        elif dummy2 == 0:
            dummy2 = 12
        bla1 = str(dummy2)
        file.close()
    with open('dummyf.txt', 'w') as file:
        file.write(bla1)
        file.close()
    return int(bla1)


def todays_month():
    # create a fake global variable to change the displayed month
    dummy2 = date.today()
    bla1 = str(int(dummy2.month))
    with open('dummyf.txt', 'w') as file:
        file.write(bla1)
        file.close()


def add_meeting(canvas):
    pass
    day_of_meeting = input('Enter the day of the meeting:(1,2,3..)')
    month_of_meeting = input('Enter the month of the meeting:(1,2,3..)')
    # creating a dictionary to add the meeting
    may_meeting = {day_of_meeting: n_meeting}


def delete_meeting(canvas):
    print('delete')


def top_rows(canvas):
    # this function present the first two line of the calendar which are the header and today's date
    # creating fake grid
    line_number = 1
    # make the header
    Header = canvas.create_text(10, LINE_GAP * line_number, fill="black", font=FONT + " bold underline",
                                text="Welcome to Leana's Calendar", anchor="nw")
    line_number += 1
    show_todays_date(canvas)


def show_meeting_buttons(canvas):
    # Fake button to add meeting
    canvas.create_rectangle(10, LINE_GAP * 15, 125, LINE_GAP * 15 + 25,  fill="light blue")
    canvas.create_text(18, LINE_GAP * 15, fill="black", font=FONT, text="Add a Meeting", anchor="nw", activefill="green")
    # Fake button to delete a  meeting
    canvas.create_rectangle(125 + 10, LINE_GAP * 15, 125 * 2 + 5, LINE_GAP * 15 + 25,  fill="light blue")
    canvas.create_text(138, LINE_GAP * 15, fill="black", font=FONT, text="Delete a Meeting", anchor="nw", activefill="green")


def show_todays_date(canvas):
    # Present today's date
    today = date.today()
    today = today.strftime("%m/%d/%y")
    today_str = "Today's date is: " + today
    todays_date = canvas.create_text(10, LINE_GAP * 2, fill="black", font= FONT + " bold", text=today_str, anchor="nw")


def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    # canvas.place()
    return canvas

def main():
    """
    New and exclusive calendar
    """
    today = date.today()
    first_day = first_day_of_year(today.year)
    todays_month()
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Calendar')
    # present the header, today's date
    top_rows(canvas)
    # present two buttons: weekly display and monthly display
    weekly = canvas.create_text(10, LINE_GAP * 3, fill="black", font= FONT, text="Weekly Display", anchor="nw", activefill="green")
    monthly = canvas.create_text(10, LINE_GAP * 4, fill="black", font="Calibri 12", text="Monthly Display ", anchor="nw", activefill="green")
    # next month text
    canvas.create_text(25 + WIDTH_GAP * 1, LINE_GAP * 4, fill="black", font="Calibri 12", text="Next Month", anchor="nw", activefill="green")
    # previous month text
    canvas.create_text(15 + WIDTH_GAP * 2, LINE_GAP * 4, fill="black", font="Calibri 12", text="Previous Month", anchor="nw", activefill="green")
    show_meeting_buttons(canvas)
    canvas.bind("<Button-1>", click_event)
    canvas.update()
    canvas.mainloop()

if __name__ == '__main__':
    main()
