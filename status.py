class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if (( a >=0 and b <0)or ( a < 0 and b>=0)) and not flag:
            return true
            
        if (a<0 and b < 0) and flag:
            return True
            
        return False    