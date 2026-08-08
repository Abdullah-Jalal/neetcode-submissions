
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for dup in nums:
            if dup not in count:
                count[dup] = 1
            else:
                count[dup]+=1

        result = (sorted(count , key = count.get , reverse = True))[:k]
        return result