class Solution:
    def isPalindrome(self, s: str) -> bool:
        # alphanumeric = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        left,right = 0, len(s)-1
        while left<right:
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            else:
                print(s[left].lower(),s[right].lower())
                if s[left].lower()!=s[right].lower():
                    return False
                left+=1
                right-=1
        return True



