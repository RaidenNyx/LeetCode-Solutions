class Solution(object):
    def lengthOfLastWord(self, s):
        res = s.strip(' ').split(" ")
        res1 = res[::-1]
        for i in range(len(res1)):
            return len(res1[0])