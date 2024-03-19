class Phone:
    manufactured = 'China'

    def __init__(self):
        pass

    def send_sms(self, phone, sms):
        text = f'sending to:{phone} {sms}'
        print(text)
