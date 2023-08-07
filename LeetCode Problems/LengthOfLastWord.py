class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(" ")
        return len(words[-1])
    
print(Solution().lengthOfLastWord("World is a beautiful place"))