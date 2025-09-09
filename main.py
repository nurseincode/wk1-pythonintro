# # print(2 + 3) # My first function comment
# # print('Hello Python!')

# # Data Types

# # Numbers
# # Int
# # 5

# # Finding the data type by calling the type function and passing the value. Output: <class 'int'>
# print(type(5))

# # Float
# # 3.14159 pi approx

# print(type(3.14159))

# # Complex Numbers
# print(type(2 + 3j))

# Number Operations
# print(2 + 3)
# print(2 - 3)
# print(2 * 3) # Multiplication asteric symbol
# print(10 / 5) # Float division. Operator always returns a float, even if the result is a whole number. Output: 2.0
# print(10 // 5) # Use integer division // if you want an integer result. Output: 2
# print(10 // 3.5) # Integer division ... sometimes. Output: 2.0 
# print(int(10 // 3.5)) # Typecasting(Converting data types) - Now output is 2
# print(5 % 2) #  Modulo operator. Gives you the remainder after division.

# Strings
# "Hello" and 'Hello' = Same
# print("She said \"It's a beautiful day\"") # Escaping. "\" escapes the quote you want to include. Output: She said "It's a beautiful day"
# print('She said "It\'s a beautiful day"')  # Or escape using single quotes to wrap the string 

# # Concatenation = Join together
# print('Python' + ' Fundamentals')

# String methods
print('Capital'.upper())
print('Python Fundamentals'.replace('Fundamentals', 'Concepts'))

# Boolean
# True
# False
print(True)
print(type(True))

# Falsy values - Treated as False in conditionals

# Common falsy values : False,None,0,0.0,'',[],{},(),set(),range(0)
print(bool(0)) # 0 evaluates to False as a boolean

# Comparison Operators
# <, >, <=, >=, == 
print(5 == 5) # Equality Operator: Is the value on the left equals to the one on the right? It returns a Boolean True/False

# Logical Operators: # and, or, not

# --> and operator : Logical AND -> Returns True if both conditions are True
# age = 20
# is_student = True
# if age > 18 and is_student:
#     print('You get a discount') <- Prints bc both conditions are True

# --> or operator: Logical OR -> Returns True if at least one condition is True

# is_monday = False
# is_weekend = True

# if is_weekend or is_monday: 
#     print('Chill!') # <- Prints bc one of the condition is True

# --> not operator: Logical NOT -> Turns True into False and vice versa

# not True -> False
# not False -> True

# is_raining = False

# if not is_raining:
#     print('Go to the Park') # <- Prints bc not False is True