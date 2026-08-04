from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for work in strs:
            random = "".join(sorted(work))
            seen[random].append(work)
        return list(seen.values())