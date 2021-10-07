## Start typing here
# get_max_distance
       A         = 0
   B       C     = 1
 D   E   F   G   = 3
 {1:[A]}
 {1:[A], 2:[B]}
 {1:[A], 2:[B], 3:[D]}
 {1:[A], 2:[B], 3:[D, E]}
 {1:[A], 2:[B, C], 3:[D, E]}
 {1:[A], 2:[B, C], 3:[D, E, F, G]}
 
 {1:1, 2:2, 3:4}
   
       A         = 0
   B       C     = 1
 D               = 0
 
        A        = 0
   B       C     = 1
 D   E       G   = 3

        A        = 0
   B       C     = 1
     E   F       = 1
     
class node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_max_distance(root):
    level_values = getLevelValues(root, height = 0, result = {})

def getLevelValues(root, height, result):
    if not root: #empty node
        placeValue = -1
    else: placeValue = root.value

    result[height] = result.get(height, []) + [placeValue]
    
    if not root.left and not root.right:
        return result
    
    getLevelValues(root.left, height + 1, result)
    getLevelValues(root.right, height + 1, result)
    return result
        
 
