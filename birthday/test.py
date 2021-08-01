import myUtilities

# Test the getName() function
testName = myUtilities.getName()
print("Hello, " + testName)

# Test the getBirthdate() function
bDay = myUtilities.getBirthdate()
print("The birthdate is " + str(bDay))

# Test the age() function
years = myUtilities.age(bDay)
print("Age is: " + str(years))
