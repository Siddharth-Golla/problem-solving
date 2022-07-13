"""You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age.
    They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Example
    candles = [4,4,1,3]

The maximum height candles are 4 units high. There are 2 of them, so return 2."""

def birthdayCakeCandles(candles):
    tall_count = 0
    max_height = max(candles)
    for value in candles:
        if value == max_height:
            tall_count = tall_count + 1
    return tall_count


if __name__ == "__main__":
    candles = [3,5,5,2,5,1,4,2]
    res = birthdayCakeCandles(candles)
    print(str(res))