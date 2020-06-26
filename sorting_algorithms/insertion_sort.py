def insertion_sort(data = []):
    n = len(data)

    for j in range (1, n):
        current = data[j]
        i = j - 1
        while i >= 0 and current < data[i]:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = current
        yield data
    return