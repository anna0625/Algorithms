def find(array, x):
    index = 0
    while index < len(array):
        if array[index] == x:
            return index
        index = index + 1

    return -1

array = [1, 2, 3, 4, 5]

print(f'index : {find(array, 3)}')

def find_recursive(array, x, low_i, high_i):
    if low_i > high_i:
        return -1
    elif array[low_i] == x:
        return low_i
    else:
        return find_recursive(array, x, low_i+1, high_i)

print(f'index : {find(array, 4)}')

