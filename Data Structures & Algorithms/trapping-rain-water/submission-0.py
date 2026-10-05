class Solution:
    def getleftMaxArray(self, height: list[int], n: int) -> list[int]:
        leftMax = [0] * n
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        return leftMax

    def getrightMaxArray(self, height: list[int], n: int) -> list[int]:
        rightMax = [0] * n
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        return rightMax

    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        n = len(height)
        leftMax = self.getleftMaxArray(height, n)
        rightMax = self.getrightMaxArray(height, n)
        
        total_water = 0
        for i in range(n):
            h = min(leftMax[i], rightMax[i]) - height[i]
            total_water += h
            
        return total_water