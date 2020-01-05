def merge_sort(a):
    if len(a) > 1:
        m = len(a) // 2
        left_part = a[:m]
        right_part = a[m:]

        merge_sort(left_part)
        merge_sort(right_part)

        i = j = k = 0
        
        n = len(left_part)
        m = len(right_part)

        while i < n and j < m:
            if left_part[i] < right_part[j]:
                a[k] = left_part[i]
                i += 1
            else:
                a[k] = right_part[j]
                j += 1
            k += 1

        while i < n:
            a[k] = left_part[i]
            k += 1
            i += 1

        while j < m:
            a[k] = right_part[j]
            k += 1
            j += 1



a = [5, 4, 3, 5, 8, -1, 0, 3, 1, 6, 33, 2, 13, 34, 56, 78]
print(a)
print(merge_sort(a))
print(a)

