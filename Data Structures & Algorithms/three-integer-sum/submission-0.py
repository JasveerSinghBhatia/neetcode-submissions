class Solution:
    result = []

    def twoSum(self, nums, target, i, j):
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1

            elif nums[i] + nums[j] < target:
                i += 1

            else:
                while i < j and nums[i] == nums[i + 1]:
                    i += 1

                while i < j and nums[j] == nums[j - 1]:
                    j -= 1

                self.result.append([-target, nums[i], nums[j]])

                i += 1
                j -= 1

    def threeSum(self, nums):
        n = len(nums)

        if n < 3:
            return []

        self.result.clear()
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            n1 = nums[i]
            target = -n1

            self.twoSum(nums, target, i + 1, n - 1)

        return self.result