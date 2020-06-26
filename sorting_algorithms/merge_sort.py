def merge_sort(data, begin, end):
    if end - begin > 1:
        middle = (begin + end) // 2
        yield from merge_sort(data, begin, middle)
        yield from merge_sort(data, middle, end)
        yield from split_merge(data, begin, middle, end)
        yield data
    return


def split_merge(data, begin, middle, end):
    left = begin
    right = middle
    result = []

    while left < middle and right < end:
        if data[left] <= data[right]:
            result.append(data[left])
            left += 1
        else:
            result.append(data[right])
            right += 1

    while left < middle:
        result.append(data[left])
        left += 1

    while right < end:
        result.append(data[right])
        right += 1

    data[begin:end] = [r for r in result]
    yield data