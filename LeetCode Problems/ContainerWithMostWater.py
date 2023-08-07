class Solution:
    def maxArea(self, height: List[int]) -> int:
        data = []
        maximum = []
        i, j = 0, 0
        while(i < len(height)-1):
            j = i+1
            while(j < len(height)):
                a = max(height[i], height[j])
                data.append(a * (j-i))
            maximum = max(data)
            data = []
        return max(maximum)