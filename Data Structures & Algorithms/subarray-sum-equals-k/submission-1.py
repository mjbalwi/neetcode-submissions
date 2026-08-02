class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        prefixSum = 0
        res = 0
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            diff = prefixSum - k
            if diff in freq:
                res += freq.get(diff)
            freq[prefixSum] = freq.get(prefixSum, 0) + 1

        return res
