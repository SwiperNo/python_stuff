numbers3 = [1, 1, 2, 3, 5, 5, 8, 13, 13, 21, 21, 21]

# Write a function to count occurrences of each element in 'numbers3'

def count_oc(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

print(f"Counts:", count_oc(numbers3))