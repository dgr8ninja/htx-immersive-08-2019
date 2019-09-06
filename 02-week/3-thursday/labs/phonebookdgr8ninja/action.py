



def show_action_result(message):
    print('===================')
    print(message)0
    print('===================')


def add():
    last_name = input('What is their last name? ')
    first_name = input('What is their first name? ')
    phone = input('What is their phone number? ')
    data.entries.append({
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone
    })
    show_action_result(f'{first_name} was added successfully')