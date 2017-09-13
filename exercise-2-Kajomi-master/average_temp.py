# -*- coding: utf-8 -*-
''' Checking the average temperature for a given month in a list.

Usage: 
    ./average_temp.py
Author:
    Mira Kajo - 13.9.2017
'''
# Printing out a month indicated in the script and the corresponding average temperature. 

# create two lists: one having the months as values, and the other the number of days in each month:
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
tempMonth = [-3.5, -4.5, -1.0, 4.0, 10.0, 15.0, 18.0, 16.0, 11.5, 6.0, 2.0, -1.5]

# set a SelectedMonth variable where the user can define which month they want to check out: 
SelectedMonth = months[8]                    

# assign the chosen months index to another variable:
MonthIndex = months.index(SelectedMonth)

# print out both the SelectedMonth and MonthIndex to check out they work:
print(SelectedMonth + " has an index of: " + str(MonthIndex))

# print out a sentence telling the month the user chose and what the average temperature is in that month:
print("The average temperature in Helsinki in", SelectedMonth, "is ", tempMonth[MonthIndex])