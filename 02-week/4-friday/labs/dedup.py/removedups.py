names = ['Alex', 'John', 'Mary', 'Steve', 'John', 'Steve']
print ("The original list is : " +  str(names)) 

def remove_duplicates(list):
    res = [] 
    for name in names: 
        if name not in res: 
            names.append(res) 

    print ("The list after removing duplicates : " + str(res)) 

