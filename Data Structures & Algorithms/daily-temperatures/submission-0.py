class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        res = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]]<temp:
                prev = stk.pop()
                res[prev] = i-prev
            stk.append(i)
        return res
        