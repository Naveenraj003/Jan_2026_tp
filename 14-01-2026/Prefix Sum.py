def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count


if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    k = int(input("Enter K: "))
    print("Number of subarrays:", subarray_sum(nums, k))
