class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s:
            if(i.isalpha()):
                arr.append(i.lower())
        arr2 = arr.copy()
        arr.reverse()
        i = 0
        while(i < len(arr)):
            if arr2[i] != arr[i]:
                return False
            i+=1
        return True
    
print(Solution().isPalindrome("race a car"))
