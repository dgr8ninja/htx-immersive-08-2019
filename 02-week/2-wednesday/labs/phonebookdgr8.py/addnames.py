from data import entries

namefirst = input("Please enter the first name you would like to add: ")

namelast = input("Please enter the last name that you would like to add: ")

add_names(namefirst + namelast)


def add_names(newname):
    oldname = []

    for name in entries:
        if name["first_name"]["last_name"] == newname:
            return name.append()
