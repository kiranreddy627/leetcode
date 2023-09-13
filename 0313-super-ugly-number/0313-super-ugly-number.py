class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        prime=primes[:]
        heapq.heapify(prime)
        a=1
        for _ in range(n-1):
            a=heapq.heappop(prime)
            for i in primes:
                heapq.heappush(prime,i*a)
                if a%i==0:
                    break
        return a