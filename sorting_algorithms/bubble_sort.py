def bubble_sort(data = []):
    n = len(data)

    while True:
        new_n = 0
        for i in range(1, n):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
                new_n = i
            yield data
        n = new_n
        if n <= 1:
            yield data
            break
    return
