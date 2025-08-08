# Last updated: 8/8/2025, 2:29:56 AM
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a=0
        for i in range(len(num)-1,-1,-1):
            a += num[i] * 10 ** (len(num) - 1 - i)
        b=a+k
        if b==0:
            return [0]
        d=[]
        while b:
            c=b%10
            d.append(c)

            b=b//10
        return d[::-1]


        