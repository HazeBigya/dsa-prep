def sort_arr(arr):
    asc = sorted(arr)
    desc = sorted(arr, reverse = True)
    print("Ascending:", asc)
    print("Descending:", desc)
    
def sort_string(str):
    asc = "".join(sorted(str.lower()))
    desc = "".join(sorted(str.lower(), reverse=True))
    print("Ascending:", asc)
    print("Descending:", desc)
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr;
                
    
arr = [10, 2, 1, 20]
str = "Banana"

sort_arr(arr)
sort_string(str)

array = [5, 3, 8, 4, 2];
print("Bubble sort Arr: ", bubble_sort(array));