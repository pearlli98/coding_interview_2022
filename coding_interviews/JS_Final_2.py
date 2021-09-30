'''
+--+--+--+
|R1    R2|
+  +  +  +
|T    |  |
+  +  +  +
|  |     |
+--+--+--+

input: board
output: sequence of (robot, direction)

16x16 grid
4 robots
'''

class Board():
    def __init__(self, width, height, robots, walls, target):
        self.width = width
        self.height = height
        self.walls = walls
        self.target = target
        
    def checkValidLanding(self, location):
        """
        return True if next position is within the board and not a robot
        False otherwise
        """
        withinBoundary = location[0] >= 0 and location[0] < self.height and location[1] >= 0 and location[1] < self.width
        notRobot = not any([location == robot for robot in self.robots])
        return withinBoundary and notRobot
    
    def noWall(loc_a, loc_b):
        return not (loc_a, loc_b) in self.walls and not (loc_b, loc_a) in self.walls
    
import deque from Queue
        
def playGame(board):
    agenda = deque([(board, [])])
    visited = set()
    while agenda:
        current_config, path = agenda.popleft()
        if current_config in visited:
            continue
        if isTarget(current_config):
            return path
        for next_config, move in getNextConfigs(current_config):
            agenda.append((next_config, path + [move]))
        visited.add(current_config)
    return None

def isTarget(board):
    return board.robots[0] == board.target

def move(currentLocation, direction):
    return (currentLocationp[0] + direction[0], currentLocation[1] + currentLocation[1])

def getNextConfigs(current_config):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = []
    for i in range(len(current_config.robots)):
        robot = current_config.robots[i]
        for dir in directions:
            current_location = robot
            next_location = move(robot, dir)
            while current_config.checkValidLanding(next_location) and current_config.noWall(current_location, next_location):
                current_location = next_location
                next_location = move(robot, dir)
            new_config = Board(current_config.width, current_config.height, current_config.robots[:], current_config.walls, current_config.target)
            new_config.robots[i] = next_location
            res.append((new_config, (i + 1, dir)))
    return res
                
            
            
    



