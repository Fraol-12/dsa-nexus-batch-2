class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       leng_last_word = s.strip().split(" ")   
       return(len(leng_last_word[-1])) 
