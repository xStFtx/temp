# from typing import List
from collections import defaultdict

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def prime_factors(num):
            factors = set()
            while num % 2 == 0:
                factors.add(2)
                num //= 2
            for i in range(3, int(num**0.5) + 1, 2):
                while num % i == 0:
                    factors.add(i)
                    num //= i
            if num > 1:
                factors.add(num)
            return factors

        def find(parents, x):
            if parents[x] == x:
                return x
            parents[x] = find(parents, parents[x])
            return parents[x]

        def union(parents, x, y):
            root_x = find(parents, x)
            root_y = find(parents, y)
            if root_x != root_y:
                parents[root_x] = root_y

        n = len(nums)
        parents = [i for i in range(n)]

        prime_factors_dict = defaultdict(list)
        for i, num in enumerate(nums):
            factors = prime_factors(num)
            for factor in factors:
                prime_factors_dict[factor].append(i)

        for factor_indices in prime_factors_dict.values():
            for i in range(len(factor_indices) - 1):
                union(parents, factor_indices[i], factor_indices[i + 1])

        root = find(parents, 0)
        for i in range(1, n):
            if find(parents, i) != root:
                return False

        return True
