'''
leetcode: https://leetcode.com/problems/partition-equal-subset-sum/solution/
[1,5,11,5]
can we divide input into 2 equal sum subets? 
True/ False
[1,5,5] [11] -> True
'''
def checkEqualSubsetSum(array):
    subsets = [] #
    for subset in subsets:
        s1 = sum([array[i] for i in subset])
        s2 = sum([array[i] for i in range(len(array)) if i not in subset])
        if s1 == s2:
            return True
    return False
    
def getSubsets(array):
    '''
    subarray vs 
    return a list of indices of subsets in the array
    '''
    if len(array) == 0:
        return []
    
    res = []
    for i in range(len(array)):
        rest = getSubsets(array[:i] + array[i + 1:])
        if not rest:
            continue
        #include
        res += [j + [i] for j in rest]
        #not include
        res += rest

    return res
