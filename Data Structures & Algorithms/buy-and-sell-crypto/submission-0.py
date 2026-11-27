class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        stk = []
        for price in prices:
            #10,7,1,5,7
            
            while stk and stk[-1]>price:
                curr = stk.pop()
            if stk:
                profit = price - stk[0]
                maxProfit = max(profit, maxProfit)
            stk.append(price)
            print(stk)
        return maxProfit
            
        