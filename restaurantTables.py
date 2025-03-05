# ------------------------------------------------------------------------------------
# The following 2D lists mimic a restaurant seating layout, similar to a grid.
# 
# - Row 0 is a "header row":
#     - The first cell (index 0) is just a row label (0).
#     - The remaining cells are table labels with capacities in parentheses,
#       e.g., 'T1(2)' means "Table 1" has capacity 2.
#
# - Rows 1 through 6 each represent a distinct "timeslot" or "seating period":
#     - The first cell in each row (e.g., [1], [2], etc.) is that row's label (the timeslot number).
#     - Each subsequent cell shows whether the table (from the header row) is
#       free ('o') or occupied ('x') during that timeslot.
#
# In other words, restaurant_tables[row][column] tells you the status of a
# particular table (column) at a particular timeslot (row).
# ------------------------------------------------------------------------------------

# Shows the structure of the restaurant layout with all tables free ("o" = open).
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'o',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'o',      'o',      'o',      'o',      'o'],
    [3,        'o',      'o',      'o',      'o',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'o'],
    [5,        'o',      'o',      'o',      'o',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'o',      'o']
]

# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------

restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]

# Level 1
def allFreeTables(tables):
    freeTables = []
    for r, row in enumerate(tables):
        for c, table in enumerate(row):
            if table == "o":
                freeTables.append((r, c))
    return freeTables
# Returns a list of tuples of each position of a free table

# Level 2
def firstFreeTableByPartySize(tables, partySize):
    for c in range(1, len(tables[0])):
        if int(tables[0][c][3]) >= partySize:
            for r in range(len(tables)):
                if tables[r][c] == "o":
                    return (r,c)
# Returns the first found valid table of sufficient size

# Level 3
def freeTablesByPartySize(tables, partySize):
    freeTables = []
    for c in range(1, len(tables[0])):
        if int(tables[0][c][3]) >= partySize:
            for r in range(len(tables)):
                if tables[r][c] == "o":
                    freeTables.append((r,c))
    return freeTables
# Returns all found valid tables of sufficient size

if __name__ == "__main__":
    print("Level 1: Position of All Free Tables: ", allFreeTables(restaurant_tables2))
    print("Level 2: Position of First Free Table By Size: ", firstFreeTableByPartySize(restaurant_tables2, 3))
    print("Level 3: Position of All Free Tables By Size: ", freeTablesByPartySize(restaurant_tables2, 3))