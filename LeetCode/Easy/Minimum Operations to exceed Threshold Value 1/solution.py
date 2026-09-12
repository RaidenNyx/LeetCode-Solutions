class Solution(object):
    def minOperations(self, nums, k):
        nums1 = []
        for i in range(len(nums)):
            if nums[i]<k:
                nums1.append(nums[i])

        return len(nums1)