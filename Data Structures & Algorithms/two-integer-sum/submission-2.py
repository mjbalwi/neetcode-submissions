class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                if i < map.get(diff):
                    return [i, map.get(diff)]
                return [map.get(diff), i]
            map[nums[i]] = i
        for k,v in map.items():
            print(k,v)
        return [0,0]
        