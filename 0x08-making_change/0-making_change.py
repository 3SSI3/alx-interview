<<<<<<< HEAD
def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize an array to store minimum coin counts
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate through each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
=======
#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
>>>>>>> c8304a1d4820b1f0fca51d142c83b26b7bd64fb2
