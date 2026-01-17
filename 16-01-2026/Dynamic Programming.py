def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    coins = list(map(int, input("Enter coin values: ").split()))
    amount = int(input("Enter amount: "))
    print("Minimum coins needed:", min_coins(coins, amount))
