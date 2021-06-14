sleepHours = int(
    input("How many hours of sleep do you require to function optimally?"))
wakeUpTime = int(
    input("what time would you like to wake up? (Enter answer as floating point)"))
if (wakeUpTime <= sleepHours):
    leftOverTime = sleepHours - wakeUpTime
    bedTime = 12 - leftOverTime
else:
    bedTime = wakeUpTime - sleepHours
print("To wake up feeling refreshed at ", wakeUpTime,
      ", make sure you goto sleep by ", bedTime)
