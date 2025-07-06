class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        rev_string = string[::-1]

        ans = (rev_string == string)

        return ans
