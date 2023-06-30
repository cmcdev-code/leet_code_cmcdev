import decimal 
num=decimal.Decimal('2.236067977499789696409173668731276235440618359611525724270897245410521')
class Solution:
    def climbStairs(self, n: int) -> int:
        return round((1/num)*(((1+num)/2)**(n+1)-(((1-num)/2)**(n+1))))
        