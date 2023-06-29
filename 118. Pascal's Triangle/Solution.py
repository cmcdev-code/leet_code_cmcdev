def choose(a,b):
    return factorial(a)//(factorial(b)*factorial(a-b))
def factorial(a):
    num=1
    if(a==0):
        return 1
    for x in range(1,a+1):
        num*=x
    return num

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li=[[1]]
        for x in range(1,numRows):
            li1=[]
            for y in range(x+1):
                li1.append(choose(x,y))
            li.append(li1)
        
        return li