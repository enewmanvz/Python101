# Order matters, The Function needs to be defined 1st before program is called
# program can be local or global

#Example: Local
#Function Definition
def greeting(name):             
    print('Hello', name)        # The Variable "name" only exits inside function where defined
                                # if "name" is defined function is is local i.e. def greeting(name)"
# Main Program                             #The program is the main body and starts running here.
input_name1 = input('Enter your name:\n')    #Example variable "name" defined in Funtion is local in scope
greeting(input_name1)                        #if local Variable "name" can Not be used in main program
input_name2 = input('Enter your name:\n')    #local allows you to reuse greeting() function with different names
greeting(input_name2)

# Example Main Global
#Function Definition
def greeting():                 #The Varible is not defined in greeting. It is now global and
    print('Hello',name)         #Can be used in the Main Program below.

# Main Program
name = input('Enter your name:\n')       #The variable Name is Global
greeting()                                 # Don't need a parameter for greeting()