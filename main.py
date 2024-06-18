from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        max_profit = 0
        max_profit_at_current_difficulty = 0
        job_index = 0
        n = len(jobs)
        
        for ability in worker:
            while job_index < n and jobs[job_index][0] <= ability:
                max_profit_at_current_difficulty = max(max_profit_at_current_difficulty, jobs[job_index][1])
                job_index += 1
            max_profit += max_profit_at_current_difficulty
        
        return max_profit
