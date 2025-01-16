# List - ordered(indexed) collection of items - mutable - can have duplicates

# Dictionary (dict) - collection of items - mutable - uordered - not indexed
# Keyed - key/value pairs - keys cannot have duplicates
# key-value pairs must be separated by commas

person1 = {
    "name": "Ngugi",
    "last_name": "Maina",
    "age": "20",
}
# hardcoded dict data but this can be fetched from an API eg fetch it as JSON by calling a method to convert to a dict
# Write my own API in python using flask framework to access and pull data from in module 4

print(person1)
# print(type(person1))
print(person1["age"]) # key error accessing age as print(person1[2]) bc dicts are not indexed
# print(person1['foo']) # Accessing a non-existent key results in an keyerror # handling these errors = exeption handling
# print(person1.get('foo')) # Accessing via a method for a non-existing key returns None instead of an error
# print(person1.get('foo', 'Key not found')) # Returns key not found instead of None - 
# get is more powerful than using square brackets

# person1['address'] = 'Melbourne' # Adding extra keys later on
# or
person1['address'] = { 'state': 'Vic', 'postcode': 3160, 'city': 'Melbourne' } # value of address is a dict
print(person1)
print(person1['address']['postcode']) # Accessing the postcode
# print(person1.address) # You can access the address via dot notation in some language eg JS, ruby but not python

print(person1)
person1.update({ 'name': 'Faith', 'age': 25, 'height': '166cms'}) # updates the key if it exists, if not its a new kv pair
print(person1)

# loop through a dict, # *rem enumerate to access an index 
# for key in person1:
#     print(f'Key: {key}')
#     print(f'Value: {person1[key]}')

# Same as above
for key, val in person1.items(): # calling items
    print(f'Key: {key}')
    print(f'Value: {val}') # Same as enumerate on a list

