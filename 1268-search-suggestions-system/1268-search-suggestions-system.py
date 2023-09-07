class Solution:
    def suggestedProducts(self, products: List[str], search: str) -> List[List[str]]:
        res=[]
        for i in range(len(search)):
            tmp=[]
            for j in products:
                if j.startswith(search[:i+1]):
                    tmp.append(j)
                tmp=sorted(tmp)[:3]
            res.append(tmp)
        return res