question: https://leetcode.com/problems/range-addition/

sol: consider storing the information only at the start and end index
thus, (1, 3, 2) can become an array (0, 2, 0, 0, -2) and then when we consecutively add the array up, we get (0, 2, 2, 2, 0). Do the same for all the updates

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * (length+1)
        
        for s, e, i in updates:
            ans[s] += i
            ans[e+1] -= i
            print(ans)
        print(ans)
        ans.pop()
        for i in range(1,length):
            ans[i] += ans[i-1]
        
        return ans
