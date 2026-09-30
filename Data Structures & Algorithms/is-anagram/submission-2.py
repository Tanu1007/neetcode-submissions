class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = [0]*26
        for i in s:
            freq1[ord(i)-ord('a')] += 1
        freq2 = [0]*26
        for i in t:
            freq2[ord(i) - ord('a')] += 1
        return freq1 == freq2
        