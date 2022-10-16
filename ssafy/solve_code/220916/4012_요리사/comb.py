def comb(arr, r):
    result = []
    if r == 1:
        for i in arr:
            result.append([i])
    elif r > 1:
        for i in range(len(arr) - r + 1):
            for j in comb(arr[i + 1:], r - 1):
                result.append([arr[i]] + j)
    return result

print(comb([1, 2, 3, 4, 5], 3))
