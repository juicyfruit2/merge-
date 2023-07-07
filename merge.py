def merge_sort_by_length(arr):
    # Base case: If the list has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_sorted = merge_sort_by_length(left_half)
    right_sorted = merge_sort_by_length(right_half)

    # Merge the sorted halves
    return merge_by_length(left_sorted, right_sorted)


def merge_by_length(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Compare the string lengths of left and right sublists
    while left_index < len(left) and right_index < len(right):
        if len(left[left_index]) >= len(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add the remaining elements from the left sublist
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Add the remaining elements from the right sublist
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Example usage
strings = ["apple", "banana", "orange", "kiwi", "grapefruit", "lemon"]
sorted_strings = merge_sort_by_length(strings)

# Print the sorted strings from longest to shortest
for string in sorted_strings:
    print(string)
