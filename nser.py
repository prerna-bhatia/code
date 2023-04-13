def next_smallest_element_right(arr):
    s = []
    res = [-1] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        while s and arr[i] < s[-1]:
            s.pop()
        if s:
            res[i] = s[-1]
        s.append(arr[i])
    return res