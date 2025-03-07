from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Step 1: Sieve of Eratosthenes to find all primes up to 10^6
        MAX = 10**6
        sieve = [True] * (MAX + 1)
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(MAX**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, MAX + 1, i):
                    sieve[j] = False
        
        # Step 2: Collect all primes within the given range [left, right]
        primes = [i for i in range(left, right + 1) if sieve[i]]
        
        # Step 3: Find the closest pair of primes
        if len(primes) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        result = [-1, -1]
        
        for i in range(1, len(primes)):
            gap = primes[i] - primes[i - 1]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i - 1], primes[i]]
        
        return result
