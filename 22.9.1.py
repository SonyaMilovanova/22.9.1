array = list(map(int, input('Введите целые числа через пробел').split()))
element = int(input('Введите любое положительное число из полученного списка'))

def merge_sort(L):  # Сортировка слиянием
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def binary_search(array, element, left, right):  #Двоичный поиск
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle-1] < element and element <= array[middle]:
        return [middle-1]
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    elif element == array[middle-1]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print('Сортированый список', merge_sort(array))

left = float(array[0])
right = float(array[-1])
if element < left or element > right:
    print('Число отсутсвует в диапазоне, выберите другое число')
else:
    print('Индекс ближайшего минимального элемента от введенного числа', binary_search(array, element, 0, len(array) - 1))
