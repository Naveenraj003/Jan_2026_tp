def activity_selection(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])
    count = 1
    last_end = activities[0][1]

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end:
            count += 1
            last_end = activities[i][1]

    return count


if __name__ == "__main__":
    start = list(map(int, input("Enter start times: ").split()))
    end = list(map(int, input("Enter end times: ").split()))
    print("Maximum activities:", activity_selection(start, end))
