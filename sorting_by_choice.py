


def findSmallest(arr: list) -> int:
    """ возвращает индекс наименьшего элемента """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr: list) -> list:
    """ возвращает отсортированный список """
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) # принимает индекс наименьшего элемента
        newArr.append(arr.pop(smallest)) # добавляет наименьший элемент в список, удаляет наименьший элемент
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))