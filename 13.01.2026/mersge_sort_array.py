def merge_sorted_arrays(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result


if __name__ == "__main__":
    a = list(map(int, input("Enter sorted array 1: ").split()))
    b = list(map(int, input("Enter sorted array 2: ").split()))
    print("Merged array:", merge_sorted_arrays(a, b))
