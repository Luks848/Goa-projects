def manual_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value

def manual_len(seq):
    count = 0
    for _ in seq:
        count += 1
    return count
