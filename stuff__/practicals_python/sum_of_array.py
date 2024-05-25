numbers = [1, 2, 3, 4, 5]

# Write a function to calculate the sum of elements in 'numbers'

def sum_of_numbers (arr):
    total = 0
    for num in arr:
        total += num
    return total

print(f"The sum of elelments: ", sum_of_numbers(numbers))
