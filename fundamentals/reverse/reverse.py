def reverse_string(str):
    length = len(str)
    S = list(str)
    L = 0
    R = length - 1
    
    while(L < R):
        [S[L], S[R]] = [S[R], S[L]]
        L += 1
        R -= 1
        
    return "".join(S)

def reserve_array(arr):
    L = 0
    R = len(arr) - 1
    
    while (L < R):
        [arr[L], arr[R]] = [arr[R], arr[L]]
        L += 1
        R -= 1
        
    return arr


str = "hello"
arr = [1, 2, 3, 4, 5]

print("The reverse of string ",str," is ",reverse_string(str))
print("The reverse of array ",arr," is ",reserve_array(arr))