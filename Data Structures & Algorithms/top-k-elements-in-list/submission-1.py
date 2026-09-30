class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        freqMap = [[] for _ in range(len(nums)+1)]
        for n in nums:
            hashmap[n]+=1
        print(freqMap)
        for key,v in hashmap.items():
            freqMap[v].append(key)
        print(freqMap)
        res=[]
        for i in range(len(nums), 0, -1):
            # res.append()
            for j in freqMap[i]:
                res.append(j)
                print(len(res))
                if len(res)==k:
                    print("hello")
                    return res
                    

        return res  


        