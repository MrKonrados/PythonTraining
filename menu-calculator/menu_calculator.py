def print_menu(menu):
    print('Menu')
    for i, v in enumerate(menu):
        print("\t{}. {} - ${}".format(i + 1, v[0], v[1]))


with open('menu.txt', 'r', encoding='utf8') as f:
    menu = f.read().splitlines()
menu = list(item.split(' - $') for item in menu)
user_input = input('\nWybierz pozycje z listy np. 321:')

price = 0
user_order = {i+1: [0, 0] for i,v in enumerate(menu)}
for order in user_input:
    value = float(menu[int(order)-1][1])
    user_order[int(order)][0] += 1
    user_order[int(order)][1] += value
    price += float(value)

# print(user_order)
print()
for k, v in user_order.items():
    # print(k, v)
    if v[0] > 0:
        print("\t{} x {:15} - ${:.2f}".format(v[0], menu[k-1][0],  v[1]))

print("-"*33)
print('\tRazem'.ljust(20)+ ' - ' + '${:.2f}'.format(price))