class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort(key=lambda x:x[0], reverse=True)
        stk = []
        for car in cars:
            pos,sp = car
            curr = (target-pos)/sp
            if not stk:
                stk.append(curr)
            else:
                if curr>stk[-1]:
                    stk.append(curr)
        return len(stk)



                

        