class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500, 
            "M" : 1000
        }
        result = values[s[0]]
        for i in range(1, len(s)):
            for j in values:
                if(s[i] == j):
                    if((s[i] == "V" or s[i] == "X") and s[i-1] == "I"):
                        result += values[j] - 2*values[s[i-1]]
                    elif((s[i] == "L" or s[i] == "C") and s[i-1] == "X"):
                        result += values[j] - 2*values[s[i-1]]
                    elif((s[i] == "D" or s[i] == "M") and s[i-1] == "C"):
                        result += values[j] - 2*values[s[i-1]]
                    else:
                        result = result + values[j]
                    break
        return result
    
print(Solution().romanToInt("MMMCDXC"))