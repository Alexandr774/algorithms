"""  быстрая сортировка """


def quicksort(array: list) -> list:
    if len(array) < 2:  # базовый случай
        return array
    else:
        pivot = array[0]  # опороный элемент
        less = [i for i in array[1:] if i < pivot]  # разделяем лист, все что меньше опорного элемента
        greater = [i for i in array[1:] if i > pivot]  # разделяем лист, все что больше опорного элемента
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([5, 8, 7, 6, 4, 2]))
