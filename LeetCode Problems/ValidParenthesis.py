class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ["{", "}", "(", ")", "[", "]"]
        for i in range(len(s)-1):
            j = brackets.index(s[i])
            if(j % 2 == 1):
                if(brackets[j+1] != s[i+1]):
                    return False
                
print(Solution().isValid("(){}()"))