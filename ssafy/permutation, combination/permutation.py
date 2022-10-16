def permutation(arr, r):
    result = []

    if r == 1:
        for e in arr:
            result.append([e])

    elif r > 1:
        for i in range(len(arr)):
            rest = [e for e in arr]
            rest.remove(arr[i])
            for p in permutation(rest, r - 1):
                result.append([arr[i]] + p)

    return result


print(permutation([1, 2, 3, 4, 5], 5))
