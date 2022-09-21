#Creating our addition Function
def addition (a, b):                    #Function Defintion
    return a + b

# Main Program                          #Main  program starts running here
num1 = float(input('Enter your 1st number:\n'))
num2 = float(input('Enter your 2nd number:\n'))
# Calling our Function
result = addition(num1, num2)

print('The result is', result)
