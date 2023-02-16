average = 0
total = 0
howManyEntered = 0
testScore = 0
print("How many test scores would you like to average?")
howMany = int(input(''))
while howManyEntered < howMany:
    print("Enter test score: ")
    testScore = int(input(''))
    total = total + testScore
    howManyEntered = howManyEntered + 1
else:
    average = total / howMany
    print("The average for the test scores is:",average)
