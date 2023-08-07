class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if(len(strs) == 1):
            return strs[0]
        i = len(strs[0]) 
        while(i > 0):
            f = True
            for string in strs:
                if(string.find(strs[0][0:i]) == -1):
                    f = False
                    break
            if(f == True):
                return strs[0][0:i]
            i-=1
        return ""
            
print(Solution().longestCommonPrefix(["hello", "hell", "Shll"]))