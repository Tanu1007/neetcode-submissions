class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+','-','*','/']
        stk=[]
        for token in tokens:
            if token not in operations:
                stk.append(int(token))
            else:
                num2 = stk.pop()
                num1 = stk.pop()
                ans=0
                if token=='+':
                    ans = num2+num1
                elif token == '-':
                    ans = num1-num2
                elif token == '*':
                    ans = num2*num1
                else:
                    ans = int(num1/num2)
                stk.append(ans)
        return stk[-1]
        