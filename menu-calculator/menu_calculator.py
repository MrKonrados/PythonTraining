"""
Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since your 
restaurant only sells 9 different items, you assign each one to a number, as shown below.

    Chicken Strips - $3.50
    French Fries - $2.50
    Hamburger - $4.00
    Hotdog - $3.50
    Large Drink - $1.75
    Medium Drink - $1.50
    Milk Shake - $2.25
    Salad - $3.75
    Small Drink - $1.25

To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate 
the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are 
ordered, the user should type in 5993348, and the program should say that it costs $19.50. Also, make sure that the 
program loops so the user can take multiple orders without having to restart the program each time.

SUBGOALS
    - If you decide to, print out the items and prices every time before the user types in an order.
    - Once the user has entered an order, print out how many of each item have been ordered, as well as the total price. 
      If an item was not ordered at all, then it should not show up.

"""


def print_bill(user_input):
    price = 0
    user_order = {i+1: [0, 0] for i,v in enumerate(menu)}
    for order in user_input:
        value = float(menu[int(order)-1][1])
        user_order[int(order)][0] += 1
        user_order[int(order)][1] += value
        price += float(value)

    print()
    for k, v in user_order.items():
        # print(k, v)
        if v[0] > 0:
            print("\t{} x {:15} - ${:.2f}".format(v[0], menu[k-1][0],  v[1]))

    print("-"*33)
    print('\tRazem'.ljust(20)+ ' - ' + '${:.2f}'.format(price))

def print_menu(menu):
    print('Menu')
    for i, v in enumerate(menu):
        print("\t{}. {} - ${}".format(i + 1, v[0], v[1]))


with open('menu.txt', 'r', encoding='utf8') as f:
    menu = f.read().splitlines()
menu = list(item.split(' - $') for item in menu)

print("Restauracja Przysmak")
print("Klawiszologia:")
print("m - wyświetl menu")
print("q - wyjście")
print("1-9 - zamowienie np. 3831")


while True:
    user_input = input('\nWybierz pozycje z listy:')
    if 'm' == user_input:
        print_menu(menu)
    elif 'q' == user_input:
        break
    else:
        try:
            int(user_input)
            print_bill(user_input)
        except ValueError:
            print('Błąd! Ciąg znaków musi zawierać tylko cyfry.')
            continue

