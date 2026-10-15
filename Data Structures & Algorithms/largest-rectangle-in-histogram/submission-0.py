class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        st = []
        n = len(heights)
        maxA = 0

        for i in range(n + 1):
            while st and (i == n or heights[st[-1]] >= heights[i]):
                height = heights[st[-1]]
                st.pop()

                if not st:
                    width = i
                else:
                    width = i - st[-1] - 1

                maxA = max(maxA, width * height)

            st.append(i)

        return maxA