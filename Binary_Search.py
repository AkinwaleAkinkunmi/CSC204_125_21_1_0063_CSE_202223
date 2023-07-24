def binary_search(arr, target):
    # We sort the array in ascending order first
    arr.sort()
    # We then set the two pointers for binary search
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 # Calculates the mid index and approximates to the nearest whole number.

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

# Example usage:
test_data = [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]
target = int(input("Enter the target: "))

index = binary_search(test_data, target)

if index != None:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the array.")





