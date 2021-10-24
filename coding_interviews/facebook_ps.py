# Welcome to Facebook!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the top bar.

# Enjoy your interview!

# //testing testing
# yes! 
# // Input: T = [68, 65, 64, 67, 69, 62]
# //    Output: [4,  2,  1 , 1,  0,  0] 

stack = [4, 5]
peek = 2
res = [4, 2, 1, 1, 0, 0]

def getDaysToWarmerTemperature(temps):
    stack = [0]
    res = [0 for i in range(temps)]
    for i in range(len(temps)):
        while stack and stack[-1] < temps[i]: #found a warmer day! 
            last_day = stack.pop()
            res[last_day] = i - last_day
        stack.append(i)
    return res
  
    
# K = 4
# X = 35
# array = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]    

# left = 0, right = 12
# mid = 6
# diff = 35 - 42 < 0

# left = 0, right = 5
# mid = 2
# diff = 35 - 22 = 13 > 0

# left = 3, right = 5
# mid = 4
# diff = 0! found it, return 4

# closest = 4
# res = [35, 39, 30, 42]
# left = 3, right = 5
# left = 3, right = 6, 30
# left = 2, right = 6, 

    
# // output: 35, 39, 30, 42
    
# time complexity: O(log n) + O(K)
# space complexity: O(K)
    

def getKClosestValuesToX(K, X, array):
    closest = binSearch(0, len(array) - 1, X, array)
    res = [array[closest]]
    
    left = closest - 1
    right = closest + 1
    
    while len(res) < K:
        if left >= 0 and left < len(array):
            if right >= 0 and right < len(array):
                if abs(X - array[left]) > abs(X - array[right]):
                    res.append(array[right])
                    right += 1
                else:
                    res.append(array[left])
                    left -= 1
            else:
                res.append(array[left])
                left -= 1
        else:
            res.append(array[right])
            right += 1
            
    # optimized
    while len(res) < K and left >= 0 and right < len(array):
        if abs(X - array[left]) > abs(X - array[right]):
            res.append(array[right])
            right += 1
        else:
            res.append(array[left])
            left -= 1
            
    if left < 0:
        res += array[right:right + (K - len(res)]
    else:
        res += array[left - (K - len(res) + 1 : left + 1]
    
    return res
                
                
    
def binSearch(left, right, X, array):
    if left == right:
        return left
    mid = int((left + right) / 2)
    diff = X - array[mid]
    if diff == 0:
        return left
    elif diff < 0:
        return binSearch(left, mid - 1, X, array)
    else:
        return binSearch(mid + 1, right, X, array)