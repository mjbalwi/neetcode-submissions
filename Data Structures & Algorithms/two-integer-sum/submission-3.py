class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                return [map.get(diff), i]
                if i < map.get(diff):
                    return [i, map.get(diff)]
                return [map.get(diff), i]
            map[nums[i]] = i
        return [0,0]
        