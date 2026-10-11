from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        dq = deque()
        result = []

        for i in range(n):
            # Step 1: Make space for nums[i]
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Step 2: Remove smaller elements from the back
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

            # Step 3: Add the current index to the deque
            dq.append(i)

            # Step 4: Store the maximum of the current window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result