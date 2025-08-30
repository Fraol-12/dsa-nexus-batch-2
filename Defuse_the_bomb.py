from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res

        ext = code * 2  # handle wrap-around easily

        if k > 0:
            # sum of the next k numbers for i = 0 is ext[1 : k+1]
            window = sum(ext[1:k+1])
            for i in range(n):
                res[i] = window
                # slide the window one step forward around the circle:
                # drop ext[i+1], add ext[i+k+1]
                window -= ext[i+1]
                window += ext[i + k + 1]
        else:
            k = -k  # number of previous items to sum
            # for i = 0, previous k are ext[n-k : n]
            window = sum(ext[n - k:n])
            for i in range(n):
                res[i] = window
                # slide as i advances:
                # outgoing = ext[i - k + n], incoming = ext[i + n]
                window -= ext[i - k + n]
                window += ext[i + n]

        return res
