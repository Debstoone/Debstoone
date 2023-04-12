# Lets learn python 

#At the begining of a file you can have multiple imports to import usefull librarys
#Example:
#import math

#This imported library allows you to use their funtions. In this case the math function. If an error occours 
#you need to install the library on your machine with a command simmilar to pip install math
#math()

#To define a function use the syntax def function_name():
#Example
def print_my_name():
    name = 'Debora' # string variable
    print(name)

print_my_name() #the function name must be called so its executed

#Lists:
#List items are enclosed in square brackets, like this [item1, item2, item3].
#Lists appear in a specific order. This enables us to use an index to access to any item.
# Lists are mutable, which means you can add or remove items after a list's creation.
# List elements do not need to be unique. Item duplication is possible, as each element has its own distinct place and can be accessed separately through the index.
# Elements can be of different data types: you can combine strings, integers, and objects in the same list.

#Tuples
#Tuples items are enclosed in curl brackets, like this (item1, item2, item3)
#The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable. This means that tuples cannot be changed while the lists can be modified.
#If you have data that shouldn’t change, you should choose tuple data type over lists since its more memory eficient

#For Loop:
#Now that we know what are lists and tuples we can you them for our loop example. We'll create a for loop
#inside a function that will print each element of a list
def my_loop():
    list=['A','B','C']
    for i in list: #for each element in list, each i, i can be any other letter or name. 
        #think of i as the iterator or a car arround the circuit. Every time it completes a lap
        # a +1 one is added. 
        print(i)

my_loop()

#Like an array a list can be accessed by its position. Like an array the index or position
#starts at 0. So printing position 1 will output Paulo
list=['Debora','Paulo','Feds']
print(list[1])

#Dictionarys is another data type. That looks like a json file. In this example the dictionary
#is called phonebook and has 3 key-value pairs.
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

#Like a list you can access a specific element. Using the dictionay_name[key] you'll get 
#the respective value. In this case we are accessing the value (phone number) for key (jack)
print(phonebook['Jack'])

#Similar to these exercises a sting is like a list. is a list of characters. So, like a list,
#you can cut it o get a specific element which would be a letter

start = "Hello, World!"
print(start[0:5]) #in this case, like on a list the 0 position is the first position
# which is the letter H and. The 5 position is not included. So it's the positions
# from 0 to 4 which output Hello

#If Else condition. In this function we declare the variable name is a string equals to Debora
#The condition will see if the name is equal to 'Debora' and output it IS Debora. If you
#change the variable name to something else it will outputits NOT Debora

def my_first_condition():
    name='Debora'
    if name == 'Debora':
        print('it IS Debora')
    else:
        print('its NOT Debora')
my_first_condition()
        
#Exception Handling
#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#These exceptions can be handled using the try statement. It this example the variable name
#is not declared. Well, its on the above function my_first_condition() right? No, wrong.
#the variable name is inside function my_first_condition() so it can only be accessed by
#that function. For that variable to be accessed on every part of the code it would need
#to be a global function. Which is a function defined outside of any function. But thats not
#the best pratic. Regarding the bellow function exception_handling() it will first
#try to print variable name, but, since that is not defined in the function, the except
#will handle the exception and print An exception occurred. You can try defining the 
#variable name inside the function and try running it again to see that now the variable
#name has output
def exception_handling():
    try:
      print(name)
    except:
      print("An exception occurred")
exception_handling()

#Parameters or Arguments:
#You can call by any one of the names. On the above example we said that global variables,
#although they are allowed, its not a best practice in python. If we want to access a variable
#from one funtion to the other we can ask the function to return that variable and then
#pass that variable as an argument to other functions
def my_sum():
    fisrt_number=10
    second_number=20
    result=fisrt_number+second_number
    print('the sum of the 2 numbers is:', result)
    return result 
result=my_sum() #In the other functions examples we just call the name of the function
#to be executed but in this case we are returning something, the result of the sum, from
#the function so we need to say that the result is equals, the output, of function my_sum

#Since we are returning the variable sum, we can now use it on a second funtion
#In the function my_subtraction() we ll pass the variable sum as an argument and use 
#it inside 
def my_subtraction(result):
    fisrt_number=50
    subtraction=fisrt_number - result
    print('number 50 minus the sum of my_sum() function is:', subtraction)
my_subtraction(result) #Like on the above funtion if we want to use the variable result
#in my_subtraction function we need to pass it as an argument/parameter when we define
#the function and when we call it



#Exercise.

#1- Create a function with a list, print the list and do a for loop printing each element

#2- Create a dictionary with at least 3 key-value pairs and print the value of the second key. 
# Then google or something how you change a value in a dictionary. I want the value of second key
#to be diferent. Then when you print the dictionary you will see that value has changed

#3- Create a funtion with an if else statement. You decide the variable and what the if statement does. 
#I want that funtion to return that variable so a second function recieves that variable as an argument and
#prints it. That print/output should be something like: 
# I am a python function and the variable i recieved was (the variable you decided in the 1s function)
