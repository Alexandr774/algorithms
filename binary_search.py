
def binary_search(list_m: list, item: int) -> int:
    low = 0
    high = len(list_m) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = list_m[mid]
        if guess == item:
            print('значение найдено')
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return steps

my_list = list(range(129))
print(binary_search(my_list, 127))