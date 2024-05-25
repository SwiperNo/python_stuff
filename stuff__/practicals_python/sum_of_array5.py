numbers2 = [100, 200, 300, 400, 500]


def cal_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total


print(f"Returned total:" , cal_sum(numbers2))
