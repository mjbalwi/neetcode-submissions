class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        result = []

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 0

        for key, val in sorted(d.items(), key=lambda x: x[1], reverse = True)[:k] :
            result.append(key)
            
        return result

                        
