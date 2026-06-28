class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.strs = strs
        hashcount = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in hashcount:
                hashcount[key] = []
            hashcount[key].append(s)
        return list(hashcount.values())