class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        d = {}
        for i in range(len(s)):
            d[s[i]] = i

        start, end = 0,0
        res = []

        for i in range(len(s)):
            end = max(end,d[s[i]])

            if (end==i):
                res.append(end-start+1)
                start = end+1


        return res