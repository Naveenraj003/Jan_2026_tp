def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


if __name__ == "__main__":
    n = int(input("Enter number of intervals: "))
    intervals = [list(map(int, input().split())) for _ in range(n)]

    result = merge_intervals(intervals)
    print("Merged intervals:")
    for interval in result:
        print(interval)
