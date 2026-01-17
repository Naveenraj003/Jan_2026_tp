def generate_subsets(nums):
    result = []

    def backtrack(index, path):
        result.append(path[:])

        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    subsets = generate_subsets(nums)

    for s in subsets:
        print(s)
