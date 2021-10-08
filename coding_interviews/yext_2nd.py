'''
Yext Engineering is moving to a new office building.
How exciting!

To ensure maximum Engineering happiness, the Yext Facilities team wants to ensure that no Engineer is too far away from a Pantry stocked with delicious and nutritious refreshments.

To help Facilities plan the layout of Engineering desks in the new office space, you will implement a program that calculates distances to the nearest Pantry.

Your program will accept a list of cells representing Pantries and a list of Blocked cells that prohibit movement.

Your program should return a blueprint according to the specifications below.


In the example blueprints below,
X - blocked cell
P - pantry

Input blueprint with Pantry and Blocked cells :

       0  1  2  3
    0     X     P
    1           X
    2  P
    3        X  P

blueprint with calculated Pantry distances :

       0  1  2  3
    0  2  X  1  P
    1  1  2  2  X
    2  P  1  2  1
    3  1  2  X  P

Expected Output blueprint in 2D integer array format :
P replaced with  0
X replaced with -1

       0  1  2  3
    0  2 -1  1  0
    1  1  2  2 -1
    2  0  1  2  1
    3  1  2 -1  0

At a distance of one from a Pantry cell are the four cells that are vertically and horizontally adjacent to the Pantry cell.


If a cell has no access to a Pantry, then it should be marked with a -2.

For example, the input blueprint below

       0  1
    0     X
    1  X  P

should result in the following output blueprint

       0  1
    0 -2 -1
    1 -1  0

since cell [0,0] has no access to the pantry at [1,1] due to all possible paths being blocked.

'''

def getBlueprint(N, blockedCells, pantryCells):

    #implement this method and any helper methods you may need

    shortestDistance = [[-2 for i in range(N)] for j in range(N)]
    
    agenda = [(i, 0) for i in pantryCells]
    visited = set()
    
    while agenda:
        currentCell, dist = agenda.pop(0) #bfs, fifo
        
        if (currentCell.row, currentCell.column) in visited:
            continue
            
        for i in currentCell.getNeighbors(N):
            if any([i.equal(j) for j in blockedCells + pantryCells]):
                continue
            agenda.append((i, dist + 1))
            
        visited.add((currentCell.row, currentCell.column))
        shortestDistance[currentCell.row][currentCell.column] = dist
        
    for cell in blockedCells:
        shortestDistance[cell.row][cell.column] = -1
        
                
    return shortestDistance
    
            
    


class Cell(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        
    def getNeighbors(self, N):
        result = []
        for row, col in [(self.row + 1, self.column), 
                         (self.row - 1, self.column),
                         (self.row, self.column + 1),
                         (self.row, self.column - 1)]:
            if row >= 0 and col >= 0 and row < N and col < N:
                result.append(Cell(row, col))
        return result
    
    def equal(self, other):
        if self.row == other.row and self.column == other.column:
            return True
        return False


def printBlueprint(blueprint, N):
    for i in range(N):
        for j in range(N):
             print(str(blueprint[i][j]).rjust(3, ' '), end = " ")
        print()


def test(testCaseNumber, N, blockedCells, pantryCells, expectedOutputBlueprint):

    blueprint = getBlueprint(N, blockedCells, pantryCells)
    if areBlueprintsIdentical(N, blueprint, expectedOutputBlueprint):
        print("Test Case " + str(testCaseNumber) + " Passed")
    else :
        print("Test Case " + str(testCaseNumber) + " Failed")


def areBlueprintsIdentical(N, bp1, bp2):
    for i in range(N):
        for j in range(N):
            if (bp1[i][j] != bp2[i][j]):
                return False
    return True


'''
-- -- -- -- -- -- -Test Case 0-- -- -- -- -- -- -

Input:

   0  1 
0
1    P

Expected Blue Print:

   0  1 
0  2  1
1  1  0

'''


blockedCells = []
pantryCells = []

pantryCells.append(Cell(1, 1))

expectedOutputBlueprintTestCase0 = [
    [2, 1],
    [1, 0],
];

test(0,
     2,
     blockedCells,
     pantryCells,
     expectedOutputBlueprintTestCase0);



'''
-- -- -- -- -- -- -Test Case 1-- -- -- -- -- -- -

Input:

   0  1  2  3  4
0
1
2        P
3
4

Expected Blue Print:

   0  1  2  3  4
0  4  3  2  3  4
1  3  2  1  2  3
2  2  1  0  1  2
3  3  2  1  2  3
4  4  3  2  3  4

'''


blockedCells = []
pantryCells = []

pantryCells.append(Cell(2, 2))

expectedOutputBlueprintTestCase1 = [
    [4, 3, 2, 3, 4],
    [3, 2, 1, 2, 3],
    [2, 1, 0, 1, 2],
    [3, 2, 1, 2, 3],
    [4, 3, 2, 3, 4]
];

test(1,
     5,
     blockedCells,
     pantryCells,
     expectedOutputBlueprintTestCase1);

'''
-- -- -- -- -- -- -Test Case 2-- -- -- -- -- -- -

Input:

   0  1  2  3
0     X     P
1           X
2  P
3        X  P

Expected Blue Print:

   0  1  2  3
0  2 -1  1  0
1  1  2  2 -1
2  0  1  2  1
3  1  2 -1  0

'''

blockedCells.clear()
blockedCells.append(Cell(0, 1))
blockedCells.append(Cell(1, 3))
blockedCells.append(Cell(3, 2))

pantryCells.clear()
pantryCells.append(Cell(2, 0))
pantryCells.append(Cell(0, 3))
pantryCells.append(Cell(3, 3))

expectedOutputBlueprintTestCase2 = [
    [2, -1, 1, 0],
    [1, 2, 2, -1],
    [0, 1, 2, 1],
    [1, 2, -1, 0]
]

test(2,
     4,
     blockedCells,
     pantryCells,
     expectedOutputBlueprintTestCase2)

'''
-- -- -- -- -- -- -Test Case 3-- -- -- -- -- -- -

Input:

   0  1  2  3  4
0
1        P
2     P  P  P
3        P  X  X
4        X

Expected Blue Print:

   0  1  2  3  4
0  3  2  1  2  3
1  2  1  0  1  2
2  1  0  0  0  1
3  2  1  0 -1 -1
4  3  2 -1 -2 -2

'''

blockedCells.clear()
blockedCells.append(Cell(3, 3))
blockedCells.append(Cell(3, 4))
blockedCells.append(Cell(4, 2))

pantryCells.clear()
pantryCells.append(Cell(2, 2))
pantryCells.append(Cell(1, 2))
pantryCells.append(Cell(3, 2))
pantryCells.append(Cell(2, 1))
pantryCells.append(Cell(2, 3))

expectedOutputBlueprintTestCase3 = [
    [3, 2, 1, 2, 3],
    [2, 1, 0, 1, 2],
    [1, 0, 0, 0, 1],
    [2, 1, 0, -1, -1],
    [3, 2, -1, -2, -2]
]

test(3,
     5,
     blockedCells,
     pantryCells,
     expectedOutputBlueprintTestCase3)


'''

-- -- -- -- -- -- -Test Case 4-- -- -- -- -- -- -

Input:

   0  1  2  3  4
0
1     X
2        X
3        P  X
4              X

Expected Blue Print:

   0  1  2  3  4
0  5  6  7  8  9
1  4 -1  8  9 10
2  3  2 -1 10 11
3  2  1  0 -1 12
4  3  2  1  2 -1

'''


blockedCells.clear()
blockedCells.append(Cell(1, 1))
blockedCells.append(Cell(2, 2))
blockedCells.append(Cell(3, 3))
blockedCells.append(Cell(4, 4))

pantryCells.clear()
pantryCells.append(Cell(3, 2))

expectedOutputBlueprintTestCase4 = [
    [5, 6, 7, 8, 9],
    [4, -1, 8, 9, 10],
    [3, 2, -1, 10, 11],
    [2, 1, 0, -1, 12],
    [3, 2, 1, 2, -1]
]

test(4,
     5,
     blockedCells,
     pantryCells,
     expectedOutputBlueprintTestCase4);




