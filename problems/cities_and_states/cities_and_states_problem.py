"""
Cities and states.

Find all cities whose first two characters are another cities state initials,
and vice versa.

Input: A file with the cities and their states.
Ouput: A file with number of matches.

Approach:
Use a dictionary to store the city and state names.
City reperesented by key,value is state
Only store the first two letter of the city name.

1. Use a int to store the amount of matches. 
2. Open and read the input file
3. Line by line, store the city as the key, and the state as value of a set
4. Then in the line: first add the pair to the dict and then compare it to see if there is a matching pair. 

For example:
Input is: ("FL", "MI", => dict = {} -> {"FL": "MI"} # will not find anything here, count = 0
           "MI", "FL",  => {"FL": "MI"} -> {"FL": "MI", "MI": "FL"}, count = 1
           "FL", "NY"  => ["MI", "NY"]
"""


from collections import namedtuple

# Data Structure
Location = namedtuple("Location", ["city", "state"])


# IO utils
def open_input(filename):
    pass


def write_output(number):
    pass


# Logic
def process():
    pass

