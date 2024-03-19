def call():
    print('calling someone i dont know')
    return 'call done'


class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'
    feature = ['camera', 'phone', 'hammer']

    def call():
        print('calling one person')
        my_phone = Phone()
        print(my_phone.features)
        my_phone.call()
