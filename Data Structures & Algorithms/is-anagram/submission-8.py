class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t

        countmap1 = {}
        countmap2 = {}
        for i in range(len(s)):
            if s[i] not in countmap1:
                countmap1[s[i]] = 1
            else:
                countmap1[s[i]] += 1
        for j in t:
            if j not in countmap2:
                countmap2[j] = 1
            else:
                countmap2[j] += 1
        if countmap1 == countmap2:
            return True
        else:
            return False

        