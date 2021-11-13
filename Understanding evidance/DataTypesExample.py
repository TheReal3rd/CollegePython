#Redacted
from random import randrange
randomString = ""

def inputValidator(valueType, message):
    while True:
        try:
            return valueType(input(message))
        except:
            print("Invalid input.")

length = inputValidator(int, "Please enter the length you wish your random string to be?\n\nLength:")#Input error handled
while length != 0:#Loop
    randomString = randomString+chr(randrange(97, 97 + 26))#This converts numbers to chars based from there decimal place (lowercase characters) Ascii table.
    #chr is a character data type. Calling it and entering a number will convert the int to chr then adding it to random string.
    #Then the random string is outputted after loop ends.
    length -= 1
print(randomString)

