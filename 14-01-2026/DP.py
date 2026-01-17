def climb_stairs(n):
    if n <= 2:
        return n

    prev1, prev2 = 2, 1
    for _ in range(3, n + 1):
        prev1, prev2 = prev1 + prev2, prev1

    return prev1


if __name__ == "__main__":
    n = int(input("Enter number of steps: "))
    print("Number of ways:", climb_stairs(n))
