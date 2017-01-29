
assignments = []

# Define some helpful global variables
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a + b for a in A for b in B]

rows = 'ABCDEFGHI'
cols = '123456789'

boxes = cross(rows, cols)

row_units = [cross(row, cols) for row in rows]
column_units = [cross(rows, col) for col in cols]
square_units = [cross(row, col) 
                for row in ['ABC', 'DEF', 'GHI'] 
                for col in ['123', '456', '789']]
diagonal_units = [[''.join(z) for z in zip(rows, cols)],
                  [''.join(z) for z in zip(rows, reversed(cols))]]
unit_list = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unit_list if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.

    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    from collections import Counter
    for unit in unit_list:
        # Collect all the twins in a unit in case there are multiple twins in one unit
        twins = [digits for digits, count in 
                Counter(values[box] for box in unit if len(values[box]) == 2).items()
                if count > 1]

        for twin in twins:
            for box in unit:
                if set(values[box]) == set(twin): 
                    # Skip if this box is eactly equal to the twin
                    # Take set in case order got mixed up
                    continue
                for digit in twin:
                    if digit in values[box]:
                        new_value = values[box].replace(digit, '')
                        assign_value(values, box, new_value)
    return values


def grid_values(grid):
    "Convert grid into a dict of {square: char} with '.' for empties."
    assert len(grid) == 81
    board = []
    digits = '123456789'
    for val in grid:
        if val in digits:
            board.append(val)
        if val == '.':
            board.append(digits)
    return dict(zip(boxes, board))

def display(values):
    "Display these values as a 2-D grid."
    width  = max(len(values[k]) for k in boxes) + 1
    for i, row in enumerate(rows):
        if i % 3 == 0:
            if i is 0:
                print('')
            else:
                print((('-' * (width) * 3 + '-+-') * 3)[:-2])
        display_row = []
        for j, col in enumerate(cols):
            bar = ''
            if j % 3 == 2 and j is not 8:
                bar = ' | '
            display_row.append(values[row + col].center(width, ' ') + bar)
        print(''.join(display_row))

def eliminate(values):
    """
    Elinate possibilities from a box if one of its 
    peers definitely already has that value.
    """
    for box, value in values.items():
        for unit in peers[box]:
            if len(values[unit]) == 1:
                value = value.replace(values[unit][0], '')
        # values[key] = value
        assign_value(values, box, value)
        
    return values

def only_choice(values):
    """
    Assign a box to a value if it's the only box 
    in a unit that could contain that value
    """

    # To reviewer - yeah this is quite clunky compared to the 
    # solution from Udacity, but I figure might as well have you 
    # reveiw the one I wrote rather than copy and paste ¯\_(ツ)_/¯
    # Thanks in advance!!

    # First find all the numbers that occur only once in a unit
    for unit in unit_list:
        occurs_only_once = set()
        occurs_more_than_once = set()
        for box in unit:
            for possibility in values[box]:
                if possibility in occurs_more_than_once:
                    continue
                elif possibility in occurs_only_once:
                    occurs_only_once.remove(possibility)
                    occurs_more_than_once.add(possibility)
                else:
                    occurs_only_once.add(possibility)

        for box in unit:
            for possibility in values[box]:
                if possibility in occurs_only_once:
                    assign_value(values, box, possibility)
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        if type(values) == type('string'):
            print('Values is {}'.format(values))
        number_solved_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        number_solved_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = number_solved_before == number_solved_after
        # Sanity check
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values
     

def solve(grid):
    return search(grid_values(grid))

def search(values):

    value = reduce_puzzle(values)
    if value is False:
        return False

    if all((len(value[k]) == 1 for k in boxes)):
        return value

    min, min_box = min((len(values[box]), box) for box in boxes if len(values[box]) > 1)
    for possibility in value[min_box]:
        new_search_values = values.copy()
        new_search_values[min_box] = possibility
        attempt = search(new_search_values)
        if attempt:
            return attempt

try:
    from visualize import visualize_assignments
    visualize_assignments(assignments)
except:
    print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
