def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      array[i], array[j] = array[j], array[i]

  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1

def quick_sort(array, low, high):
  if low < high:
    pi = partition(array, low, high)

    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)




size = int(input("This is the selection sort algorithm practice \nPlease enter the size of the array to be sorted : "))
arr = list(range(size))
for i in arr:
    arr[i] = int(input("element {}: ".format(i)))
    
    
print("After Sorting :-")
quick_sort(arr, 0, size - 1)
print(arr)