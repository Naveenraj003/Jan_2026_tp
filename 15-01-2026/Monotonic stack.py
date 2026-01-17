def next_greater_elements(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)

    return result


if __name__ == "__main__":
    arr = list(map(int, input("Enter array: ").split()))
    print("Next Greater Elements:", next_greater_elements(arr))
