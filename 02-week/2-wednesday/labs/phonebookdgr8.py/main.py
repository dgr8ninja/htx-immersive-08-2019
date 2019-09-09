from data import entries
# import lookup
# import deletename
# import allentries
# import addnames


def phonebookmain():
    print("Electronic Phone Book")
    print("=====================")
    print("1. Look up an entry")
    print("2. Add an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")

def look_up_by_first(firstname):

    for name in entries:
        if name["first_name"] == firstname:
            print(name)

def look_up_by_last(lastname):

    for name in entries:
        if name["last_name"] == lastname:
            print(name)

def entry_to_add():
    namenumphone = {}

    entername = input("Please enter the first name of the person you would like to add: ")
    namenumphone['first_name'] = entername
    enterlast = input("Please enter the last name of the person you would like to add: ")
    namenumphone['last_name'] = enterlast
    enterphone = input("Please enter the phone number of the person you would like to add: ")
    namenumphone['phone'] = enterphone
    entries.append(namenumphone)
    print(entries)

def list_of_entries():

    for allnames in entries:
        print(allnames)

phonebookmain()

choice = input("Please input the number that you would like to use: ")
    #come back and error check
if choice == "1":
    lookupchoice = input("Please enter First, Last,or Phone: ")
    if lookupchoice == "First":
        name = input('Please enter the first name of the person you are looking for: ')
        look_up_by_first(name)
    elif lookupchoice == "Last":
        name = input('Please enter the Last name of the person you are looking for: ')
        look_up_by_last(name)
if choice == "2":
    entry_to_add()






    





