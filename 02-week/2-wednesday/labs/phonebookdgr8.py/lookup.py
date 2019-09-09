from data import entries


name = input('Please enter the first name of the person you are looking for: ')
look_up_by_first(name)


def look_up_by_first(firstname):
    
    first = []

    for name in entries:
        if name["first_name"] == firstname:
            print(name)

def look_up_by_last(lastname):
    
    last = []

    for name in entries:
        if name["last_name"] == lastname:
            print(name)
        
def look_up_by_phone(phonenum):
        
    num = []

    for number in entries:
        if number["phone"] == phonenum:
            print(number)  
