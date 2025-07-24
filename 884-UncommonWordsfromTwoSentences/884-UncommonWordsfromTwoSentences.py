# Last updated: 7/23/2025, 6:04:42 PM
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        a=s1.split()+s2.split()
        d={}
        b=[]
        for i in range(0,len(a)):
            if a[i] not in d:
                d[a[i]]=1
            else:
                d[a[i]]+=1
        for key,value in d.items():
            if value==1:
                b.append(key)
        return b


