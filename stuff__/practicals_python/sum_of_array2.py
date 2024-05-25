numbers = [1, 2, 3, 4, 25]

# Write a function to calculate the sum of elements in 'numbers'

def cal_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total


print(f"Total amount:", cal_sum(numbers))