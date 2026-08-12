# Time Complexity: O(log n)
# Space Complexity: O(1)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

arr = [11, 12, 22, 25, 34, 64, 90]
target = 25
print("Input array:", arr)
print("Target element:", target)

result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
