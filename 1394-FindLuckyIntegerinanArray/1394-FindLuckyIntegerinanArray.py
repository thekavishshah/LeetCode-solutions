# Last updated: 7/8/2025, 11:51:59 PM
class Solution(object):
    def findLucky(self, arr):
        d={}
        b=[]
        for i in range(0,len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        for key,value in d.items():
            if key==value:
                b.append(key)
        if b:
            return max(b)
        else:
            return -1