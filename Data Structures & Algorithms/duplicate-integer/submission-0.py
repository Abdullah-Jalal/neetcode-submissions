class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for dup in nums:
            if dup in seen:
                return True
            seen.add(dup)
        return False    