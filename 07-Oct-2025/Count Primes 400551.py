# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        prime = [True for i in range(n)]
        prime[0] = prime[1] = False

        i = 2 
        while i < n:
            if prime[i]:
                j = i * 2
                while j < n:
                    prime[j] = False
                    j += i

            i += 1
        count = 0
        for i in range(len(prime)):
            if prime[i]:
                count += 1

        return count

