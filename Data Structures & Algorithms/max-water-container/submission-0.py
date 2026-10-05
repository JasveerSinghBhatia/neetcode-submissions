class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        i,j = 0, n-1
        maxWater = 0
        while(i<j):
            width = j-i
            height = min(heights[i], heights[j])
            maxWater = max(maxWater, (width * height))

            if heights[i]> heights[j]:
                j -= 1
            else:
                i += 1
        return maxWater