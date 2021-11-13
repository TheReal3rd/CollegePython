def inputFloat(outputText):
	valid = False
	while valid == False:
		try:
			returnValue = float(input(outputText))
			valid = True
		except:
			print("Invalid Input.")
			valid = False
	return returnValue

def calcRepayments(loanAmount2, monthInterest2, numPayments2):
	returnResult = monthInterest2 * loanAmount2 / 1 - (1 + monthInterest2) * numPayments2
	return returnResult

while __name__ == "__main__":
	loanAmount = inputFloat("Please enter the Loan Amount.\n")
	monthInterest = inputFloat("Please enter the Monthly rate of interest.\n")
	numPayments = inputFloat("Please enter the Number of Payments.\n")
	result = calcRepayments(loanAmount,monthInterest,numPayments)
	print(str.format("The result is:{:.2f}",result))