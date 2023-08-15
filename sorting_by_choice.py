def find_smallest(arr: list) -> int:
    """ возвращает индекс наименьшего элемента """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    """ возвращает отсортированный список """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # принимает индекс наименьшего элемента
        new_arr.append(arr.pop(smallest))  # добавляет наименьший элемент в список, удаляет наименьший элемент
    return new_arr


print(selection_sort([5, 3, 6,2,4,62,35, 2, 10]))
