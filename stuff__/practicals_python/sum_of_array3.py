numbers2 = [10, 20, 30, 40, 50]

# Write a function to calculate the sum of elements in 'numbers2'
def cal_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

print(f"Total:", cal_sum(numbers2))