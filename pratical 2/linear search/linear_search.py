# Time Complexity: O(n)
# Space Complexity: O(1)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [64, 34, 25, 12, 22, 11, 90]
target = 25
print("Input array:", arr)
print("Target element:", target)

result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
