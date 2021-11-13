
def inputValidator(message, dataType):
    while True:
        try:
            return dataType(input(message))
        except:
            print("Error! invalid input try again please.")

def splitter(arrayIn):
    returnArray = []
    for x in arrayIn:
        returnArray.append(x.sales) 
    returnArray.sort()
    return returnArray

def worstSorter(arrayIn):#Easiest method of sorting an array with an objects or pairs.
    sortedArray = splitter(arrayIn)
    returnArray = []
    for x in sortedArray:
        for y in arrayIn:
             if x == y.sales:
                 returnArray.append(y)
    returnArray.reverse()
    return returnArray

class employeeObject():
    name = ""
    i_d = -1
    sales = -1
    commission = -1.00
    def __init__(self, name, i_d, sales):
        self.name = name
        self.i_d = i_d
        self.sales = sales
        self.commission = round(sales * 500, 2)

employeeInfoList = []
numOfEmployees = inputValidator("Please enter the number of employees: ", int)
while numOfEmployees > 0:
    name = inputValidator("Please enter the employee name: ", str)
    i_d = inputValidator("Please enter the employee ID: ", int)
    sales = inputValidator("Please enter the number of houses sold: ", int)
    newObject = employeeObject(name, i_d, sales)
    employeeInfoList.append(newObject)
    numOfEmployees-=1
employeeInfoList = worstSorter(employeeInfoList)
#Add the 15% bonus to the highest value.
commissionTemp = employeeInfoList[0].commission
employeeInfoList[0].commission = round((commissionTemp / 15) + commissionTemp,2)

totalCost = 0.00
for x in employeeInfoList:#Output the employees information & add them to create the total.
    totalCost+= x.commission
    print(str.format("Name: {name} ID: {i_d} Sales: {sales} Commission: £{commission}", name = x.name, i_d = x.i_d, sales = x.sales, commission = x.commission))
totalCost = round(totalCost, 2)
print("The total cost is: £", totalCost)

