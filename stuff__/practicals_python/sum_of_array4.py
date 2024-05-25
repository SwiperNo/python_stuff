numbers3 = [-1, 0, 1, 2, -2, 3]

# Write a function to calculate the sum of elements in 'numbers3'

def cal_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(f"Total:", cal_sum(numbers3))