ex =( '.com', '.ru', '.net')
def send_email (message, recipient,*,sender ='university.help@gmail.com'):
    if recipient.endswith(ex) and sender.endswith(ex):
        if '@' in recipient and sender:
            if sender == recipient:
                print('Нельзя отправить письмо самому себе')
            else:
                if  sender == 'university.help@gmail.com':
                     print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
                else:
                     print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')






send_email('dhdk','fhfj@kfg')
send_email('djcnfhf','university.help@gmail.com')
send_email('fkglgj','dkfkgk@kfl.ru',sender='dkflgl@fjgj.com')
send_email('fjgk','fkglgl@fjhk.ru')