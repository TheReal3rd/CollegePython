#Redacted
from random import randint

def inputValidator(valueType, message):
    while True:
        try:
            return valueType(input(message))
        except:
            print("Invalid input!")


while __name__ == "__main__":
    #Float to Int
    floatValue = 50.5
    intValue = int(floatValue)
    print(intValue," Float to Int \n")
    #Int to Float
    intValue = 60
    floatValue = float(intValue) + 0.5
    print(floatValue," Int converted to a float then added 0.5")
    #Float converted to string.
    stringValue = str(floatValue)+" To string!"
    print(stringValue)
    #Float to string using formatting.
    stringValue = str.format("Float value {float}", float = floatValue)
    print(stringValue)
    #Boolean converting
    booleanValue = True
    intValue = int(booleanValue)
    print(str.format("Boolean to string: {boolean} Boolean to int {intBoolean}", boolean = booleanValue, intBoolean = intValue))
    #Bytes converting
    bytesValue = bytes(True)
    print(bytesValue)
    break

