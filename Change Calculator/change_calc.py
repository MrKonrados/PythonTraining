"""
BASIC GOAL Imagine that your friend is a cashier, but has a hard time counting back change to customers. 

Create a program that allows him to input a certain amount of change, and then print how how many quarters, dimes, 
nickels, and pennies are needed to make up the amount needed.

For example, if he inputs 1.47, the program will tell that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.

SUBGOALS
    1.  So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money 
        given to him and the price of the item. The program should then tell him the amount of each coin he needs 
        like usual.
    2.  To make the program even easier to use, loop the program back to the top so your friend can continue to use 
        the program without having to close and open it every time he needs to count change.
"""

from decimal import Decimal

coins = {
    'quarter': Decimal(.25),
    'dime': Decimal(.10),
    'nickel': Decimal(.05),
    'penny': Decimal(.01),
}

amount_money = Decimal(4.21)
price = Decimal(1.47)

price = amount_money - price

change = {}
for coin in sorted(coins, key=coins.__getitem__, reverse=True):
    div, mod = divmod(price, coins[coin])
    change[coin] = int(div)
    price = Decimal(price) - Decimal(coins[coin] * div)


for c in change:
    print(c,"\t=\t", change[c])