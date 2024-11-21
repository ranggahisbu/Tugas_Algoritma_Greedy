def hitung_kombinasi_koin(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1  

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] += dp[i - coin]

    return dp[target]

coins = [2, 3, 5, 10, 15]
target = 7
print(f"Jumlah kombinasi untuk mencapai {target} adalah {hitung_kombinasi_koin(coins, target)}")
