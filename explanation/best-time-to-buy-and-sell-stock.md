# Best Time to Buy and Sell Stock

## Single Pass

Maximum profit from current stock is `max(right subrray of prices[i]) - price[i]`.

So iterate the array from right to left.

Maintain two variables - `max_right` and `max_profit`.

If `max_right - price[i]` is greater than `max_profit`, update it.

This is the favorable stock that we need to buy.

If current stock price is greater than `max_right`, update it.

This might be of use to the stocks that are on the left of current stock.


