# create clockTime class
class clockTime:
    # create attributes for hours, minutes, seconds and initialise to 0
    hours = 0
    minutes = 0
    seconds = 0

    # method for setting hours
    def setHours(self, hours):
        self.hours = hours
    
    #method for setting minutes
    def setMinutes(self, minutes):
        self.minutes = minutes
    
    # method for setting seconds
    def setSeconds(self, seconds):
        self.seconds = seconds

    # method for setting hours, minutes, seconds
    def setTime(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # method to display time
    def showTime(self):
        print("The time is {hours}:{minutes}:{seconds}".format(hours=self.hours, minutes=self.minutes, seconds=self.seconds))

# create an object for clockTime class    
clockTimeObject = clockTime()

# prompt user for input for hours
hoursInput = int(input("Enter value for hours: "))
# validate if hours is between 0 and 24, if not, prompt user for input again
while (hoursInput < 0) or (hoursInput > 24):
    print("Invalid input, please try again.")
    hoursInput = int(input("Enter value for hours: "))

# prompt user for input for minutes
minutesInput = int(input("Enter value for minutes: "))
# validate if minutes is between 0 and 60, if not, prompt user for input again
while (minutesInput < 0) or (minutesInput > 60):
    print("Invalid input, please try again.")
    minutesInput = int(input("Enter value for minutes: "))

# prompt user for input for seconds
secondsInput = int(input("Enter value for seconds: "))
# validate if seconds is between 0 and 60, if not, prompt user for input again
while (secondsInput < 0) or (secondsInput > 60):
    print("Invalid input, please try again.")
    secondsInput = int(input("Enter value for seconds: "))

# set the hours, minutes, seconds attributes for clockTimeObject
clockTimeObject.setTime(hoursInput, minutesInput, secondsInput)

# display the time for clockTimeObject
clockTimeObject.showTime()