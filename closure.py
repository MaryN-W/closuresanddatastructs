# Closure
# A function that returns another function
# The returned information retains a copy of the scope of the outer function

def greet(name):
    print('Hello')
    def display_name():
        print(name)
    return display_name # Returning creates a closure


spam = greet('Wangari')
print(type(spam))
spam() # Call the function stored in spam
