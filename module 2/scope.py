balance = 3000


def buy_things(item, price):
    balance = balance - price
    print(f'balance after buying {item}', balance)


buy_things('sunglass', 1000)
