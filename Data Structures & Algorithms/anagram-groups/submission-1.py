class Solution:
    def getKey(self, st):
        arr = [0]*26
        for s in st:
            arr[ord(s)-ord('a')]+=1
        return tuple(arr)

        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = {}
        for st in strs:
            if self.getKey(st) not in hashmap.keys():
                hashmap[self.getKey(st)] = []
            hashmap[self.getKey(st)].append(st)
        
        return list(hashmap.values())
