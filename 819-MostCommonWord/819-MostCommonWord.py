# Last updated: 8/6/2025, 3:30:35 AM
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        d={}
        b=paragraph.lower()
        for p in string.punctuation:
            b = b.replace(p, " ")
        a=b.split()
        for i in a:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for word in banned:
            if word in d:
                d.pop(word)
        result=max(d,key=d.get)
        return result
            

        