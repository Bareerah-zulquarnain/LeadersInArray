def leaders(a,a_size):
    max_from_right = a[a_size-1]
    print(max_from_right,end=" ")
    for i in range(a_size-2,-1,-1):
        if max_from_right <= a[i]:
            max_from_right = a[i]
            print(max_from_right,end=" ")
a = [16, 17, 4, 3, 5, 2]
a_size = len(a)
leaders(a, a_size)