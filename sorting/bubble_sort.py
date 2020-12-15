def bubble_sort(arr):
    for index in range(len(arr)-1, 0, -1):
        for i in range(index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

if __name__ == '__main__':
    test_list = [5, 3, 9, 10, 2, 7, 8, 8, 6, 13]
    print(bubble_sort(test_list))