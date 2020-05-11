#!/usr/bin/python

from sys import argv

input_file = '/home/jay/code/testing/sql/populate_tables.sql'
cards_output_file = '/home/jay/code/testing/sql/cards_table_populate.sql'
line_start = False

cards = []
tokens = []
prices = []
rulings = []
legalities = []
foreign_data = []
set_translations = [] 

insertion_string = ''
#What this script would ideally do is save the entire INSERT part of the original file
#in memory, and then iterate through it, applying the logic below, appending insert strings
#into their respective lists, then, finally, going back through and appending the lists in the order
#of table creation -> sets -> cards -> tokens -> etc, etc. to an actual file to be ran for the insert.
for line in open(input_file, 'r'):
    temp = line.split()
    if len(temp) > 2:
        if temp[2] == 'cards' and temp[0] == 'INSERT':
            if ';' in line:
                insertion_string += line
                cards.append(insertion_string)
                insertion_string = ''
            else:
                insertion_string += line.rstrip()
                line_start = True
        elif line_start:
            if ';' in line:
                cards.append(insertion_string)
                insertion_string = ''
                line_start = False
            else:
                insertion_string += line.rstrip()

with open(cards_output_file, 'w') as cards_out:
    for line in cards:
        cards_out.write(line)
cards_out.close()
