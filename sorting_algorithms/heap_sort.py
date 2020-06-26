def heap_sort(data=[]):
    n = len(data)
    middle = n // 2
    # build a max-heap
    for i in range (middle, -1, -1):
        yield from heapify(data, i, n)

    for i in range (n-1, 0, -1):
        data[0], data[i] = data[i], data[0]
        yield from heapify(data, 0, i)
    return

# create a heap of size end - begin
def heapify(data, begin, end):
    root = begin
    left = 2 * root + 1
    right = left + 1

    if left < end and data[begin] < data[left]:
        root = left

    if right < end and data[root] < data[right]:
        root = right

    if root != begin:
        data[begin], data[root] = data[root], data[begin]
        yield from heapify(data, root, end)
    yield data