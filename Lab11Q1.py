# create calculator class
class Calculator:
    # method for adding input1 and  input2
    def adder(self, input1, input2):
        return input1 + input2

    # method for subtracting input2 from input1
    def subtractor(self, input1, input2):
        return input1 - input2

    # method for multiplying input1 by input2
    def multiplier(self, input1, input2):
        return input1 * input2

    # method for dividing input1 by input2
    def divider(self, input1, input2):
        return input1 / input2

    # method to clear data in input1 and input2
    def clear(self, input1, input2):
        input1 = 0
        input2 = 0

# create an object for calculator class
calculatorObject = Calculator()

# prompt user for input1 and input2
input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))

# display results for all operations done on input1 and input2
print("The output for adder() is " + str(calculatorObject.adder(input1, input2)))
print("The output for subtractor() is " + str(calculatorObject.subtractor(input1, input2)))
print("The output for multiplier() is " + str(calculatorObject.multiplier(input1, input2)))
print("The output for divider() is " + str(calculatorObject.divider(input1, input2)))

# clear input1 and input2
calculatorObject.clear(input1, input2)