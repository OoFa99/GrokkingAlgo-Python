def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if(data[min_index] > data[j]):
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

#########################

arr = [5, 3, 6, 2, 10]
print(selection_sort(arr))