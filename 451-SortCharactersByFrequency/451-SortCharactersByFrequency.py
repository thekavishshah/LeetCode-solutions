# Last updated: 7/25/2025, 12:00:55 AM
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}
        a=""
        for i in range(0,len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)

        for key, value in sorted_items:
            a += key * value

        return a



        
        