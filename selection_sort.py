def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if(data[min_index] > data[j]):
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

#########################
size = input("This is the selection sort algorithm practice \nPlease enter the size of the array to be sorted : ")
arr = list(range(int(size)))
for i in arr:
    arr[i] = int(input("element {}: ".format(i)))
    
    
print("After Sorting :-")
print(selection_sort(arr))