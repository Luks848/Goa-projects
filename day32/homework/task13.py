def n_to_array(n):
    result = []
    for number in range(1, n + 1):
        if number % 2 == 0:
            result.append(number)

    return result

