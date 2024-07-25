class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort(arr, left, mid)
                merge_sort(arr, mid + 1, right)
                merge(arr, left, mid, right)

        def merge(arr, left, mid, right):
            left_half = arr[left:mid+1]
            right_half = arr[mid+1:right+1]
            
            i = j = 0
            k = left
            
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
            
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
            
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        merge_sort(nums, 0, len(nums) - 1)
        return nums