def reverse_array(arr):
    n = len(arr)
    l=[]
    for i in range(1,n+1):
        l.append(arr[-(i)])
    return l
arr = list(map(int,input("Enter the List: ").split()))
print(reverse_array(arr))
