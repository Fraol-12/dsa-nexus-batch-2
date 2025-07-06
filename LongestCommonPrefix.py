class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        relative = strs[-1]

        for i in range(len(relative)):
            for s in strs:
                if i == len(s) or s[i] != relative[i]:
                    return "".join(res)
            res.append(s[i])
        return "".join(res)
