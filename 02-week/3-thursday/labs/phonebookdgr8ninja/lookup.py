


def lookupbyname (name):
    results = []
    for entry in entries:
        if name == entry['first_name']:
            results.append(entry)
        elif name == entry['last_name']:
            results.append(entry)
    return results

def look_up_by_id (unique):
    results = []
    for entry in entries:
        if unique == entry['unique_id']:
            results.append(entry)
    return results

def look_up_by_email (email_entry):
    results = []
    for entry in entries:
        if email_entry == entry['email']:
            results.append(entry)
    return results

        

