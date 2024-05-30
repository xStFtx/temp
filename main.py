class Solution:
    def countTriplets(self, arr):
        n = len(arr)
        # Compute prefix_xor array
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        count = 0
        # Check for each combination of i and k
        for i in range(n):
            for k in range(i + 1, n):
                if prefix_xor[i] == prefix_xor[k + 1]:
                    count += (k - i)
        
        return count
