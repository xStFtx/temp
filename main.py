from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)
        
        # Get the maximum frequency
        max_frequency = max(task_counts.values())
        
        # Count the number of tasks that have the maximum frequency
        max_frequency_tasks = list(task_counts.values()).count(max_frequency)
        
        # Calculate the minimum number of intervals required
        minimum_intervals = (max_frequency - 1) * (n + 1) + max_frequency_tasks
        
        # Return the maximum of either the minimum intervals or the length of the tasks array
        return max(minimum_intervals, len(tasks))
