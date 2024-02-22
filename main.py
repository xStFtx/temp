from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Arrays to track in-degree and out-degree of each person
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)

        # Count in-degrees and out-degrees based on the trust relationships
        for t in trust:
            out_degree[t[0]] += 1
            in_degree[t[1]] += 1

        # Check for the person with in-degree (n-1) and out-degree 0
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i

        return -1  # Town judge not found