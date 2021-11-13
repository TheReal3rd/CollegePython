#Redacted
from random import randint

#Navigational
def inputValidator(message, valueType):
    while True:
        try:
            return valueType(input(message))
        except:
            print("Invalid Input!")

#Array - 1
def arrayExample():
    array = [] #Creation of the array.
    print("Creation of the array here:\n")
    while len(array) != 10:
        array.append(randint(1,100)) # Resizes the array (Adds 10 random values.)

    for x in array:
        print(x)

    print("Sorted array here:\n")
    array.sort() # Sorts the array.

    for x in array:
        print(x)

#List - 2
def listExample():
    listData = list(()) # Creation of the list.
    while len(listData) != 10:
        listData.append(randint(1,100))

    for x in listData:
        print(x)
    
    listData[1:4] = [4,5,99]#Changes a range of values. 

    for x in listData:
        print(x)

#Tuple - 3
def tupleExample():
    tupleData = (1,"testData2",10.5)# Creation of the tuple

    print("Tuple data here:\n")
    for x in tupleData:
        print(x)

    print("Tuple unpacked data here:\n") # Unpacking a tuple example
    (a, b, c) = tupleData
    print(a)
    print(b)
    print(c)

while True:
    manuSelection = inputValidator("Array - 1\nList - 2\nTuple - 3\nPlease Enter witch list type you want to test.", int)
    if(manuSelection == 1):#Array
        arrayExample()
    elif(manuSelection == 2):#List
        listExample()
    elif(manuSelection == 3):#Tuple
        tupleExample()
    else:
        print("You entered a invalid menu selection.\nTry Again.\n")
