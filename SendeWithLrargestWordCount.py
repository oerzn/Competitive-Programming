class Solution(object):
    def largestWordCount(self, m, s):
        D = {}
        for idx, s in enumerate(s):
            if s not in D:
                D[s] = len(m[idx].split())
            else:
                D[s] += len(m[idx].split())
        count = max(D.values())
        largest_s = self.k(D, count)
        return sorted(largest_s)[-1]

    def k(self, D, count):
        largest_s = [k for k, v in D.items() if v == count]
        return largest_s
            