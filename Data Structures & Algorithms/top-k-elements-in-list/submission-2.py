class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        for key, value in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]:
            result.append(key)

        return result

        
        