import heapq

def kth_largest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    k = int(input("Enter k: "))
    print("Kth largest element:", kth_largest(nums, k))
