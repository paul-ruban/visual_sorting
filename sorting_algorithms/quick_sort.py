def quick_sort(data, begin, end):
    if begin < end:
        i = begin
        pivot = data[end]

        for j in range (begin, end):
            if data[j] < pivot:
                data[i], data[j] = data[j], data[i]
                i += 1
            yield data
        data[i], data[end] = data[end], data[i]
        yield data
        yield from quick_sort(data, begin, i-1)
        yield from quick_sort(data, i + 1, end)
    return