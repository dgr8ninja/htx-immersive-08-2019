phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
} 

print(phonebook_dict['Elizabeth'])

phonebook_dict.update( {'Kareem': '938-489-1234'} ) 

print(phonebook_dict)

result = phonebook_dict.pop("Alice")    
 
print("Deleted item's value = ", result)
print("Updated Dictionary :" , phonebook_dict)


  
# printing initial json 
print ("initial 1st dictionary", phonebook_dict) 
  
# changing keys of dictionary 
phonebook_dict.update({"Bob": '968-345-2345'})
  
# printing final result 
print ("final dictionary", str(phonebook_dict)) 

print(phonebook_dict.values())


# Exercise 2

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  
  'friends': [
    {
    'name': 'Jasmine',
    'email': 'jasmine@yahoo.com',
    'interests': ['photography', 'tennis']
  
  },
     
     {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
     }
    ]
}

email_name = ramit['email']

email = {}
print(email_name)



interest_name = ramit['interests'][0]

int_erests = {}
    
print(interest_name)



jas_email = ramit['friends'][0]['email']

jasmine = {}

for friend in ramit['friends']:
    if friend['email'] == 'jasmine@yahoo.com':
        
        jasmine = friend
        
print(jasmine['email'])


jan_interests = ramit['friends'][1]['interests'][1]

jan_dict = {}

for friend in ramit['friends']:
    if friend['interests'] == 'tv':
        jan = friend
        
print(jan_dict['interests'])
