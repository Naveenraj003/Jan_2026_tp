def longest_subarray_sum_k(arr, k):
    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    arr = list(map(int, input("Enter array: ").split()))
    k = int(input("Enter K: "))
    print("Longest subarray length:", longest_subarray_sum_k(arr, k))
