class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ty=customers.count("Y")
        tn=0
        mini=10**9
        for i in range(len(customers)):
            if ty+tn<mini:
                mini=ty+tn
                res=i
            if customers[i]=="Y":
                ty-=1
            else:
                tn+=1
        if ty+tn<mini:
            mini=ty+tn
            res=len(customers)
        return res