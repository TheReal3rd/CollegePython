from datetime import date
menuText = "1 : Help \n2 : Add entry \n3 : Display\n4 : Save \n5 : Exit program and save \n"
salesEntries = list(())

def inputValidator(message,valueType):#Handles syntax errors
    while True:
        try:
            return valueType(input(message))
        except:
            print("Invalid Value...")

def saveToFile(arrayIn):
    textFile = open("carsales_{date}".format(date = date.today()),"a")
    for x in salesEntries:
        textFile.write("\nName:{name} | SoldCars:{sales}".format(name = x[0], sales = x[1]))
    textFile.close()

# Learning how to create sorting algorithms. ~~:)~~ ;_; pain!
def betterSorter(arrayIn):# Complete
    def swapPair(index1, index2):
        pair = arrayIn[index1]
        pair1 = arrayIn[index2]
        arrayIn[index1] = pair1
        arrayIn[index2] = pair
    counter = -1
    swapped = True
    while swapped:
        swapped = False
        counter+=1
        for x in range(1, len(arrayIn)-counter):
            if arrayIn[x - 1][1] < arrayIn[x][1]:
                swapPair(x - 1, x)
                swapped = True
    return arrayIn

while __name__ == "__main__":
    selection = inputValidator("Please enter witch option you wish to use.\nIf you need help enter 1\nSelection:", int)
    if selection == 1:#Help
        print(menuText)
    elif selection == 2:#Add entries
        numberOfEntries = inputValidator("Please enter how many entries you wish to enter.\nEntries:", int)
        while numberOfEntries != 0:
            name = inputValidator("Please enter the name of the employee.\nName:", str)
            isValid = False
            while isValid == False:
                sales = inputValidator("Please enter the number of cars this employee has achived this week.\nSold:", int)
                if sales > 0:
                    isValid = True
            salesEntries.append((name, sales))
            numberOfEntries -= 1
        salesEntries = betterSorter(salesEntries)
    elif selection == 3:#Display
        for x in salesEntries:
            print("Name: {name} Sales: {sales}".format(name = x[0], sales = x[1]))
    elif selection == 4:#Save
        if(len(salesEntries) <= 0):
            print("There are no entries to save.")
        else:
            saveToFile(salesEntries)
    elif selection == 5:#Save And exit
        if(len(salesEntries) <= 0):
            print("There are no entries to save.\nExiting...")
            break
        else:
            print(salesEntries)
            saveToFile(salesEntries)
            exit()
    else:
        print("Invalid selection.\nTry option 1 for help information.")


