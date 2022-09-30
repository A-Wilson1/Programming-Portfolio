
#task 1
print('Hello world')
#task 2
print('Hello, Ashley!')
#task 3
Celsius = 38.4
Fahrenheit = (Celsius * 9/5) + 32

print('Over the summer, temperatures in Yorkshire reached '+str(Celsius)+'C which is '+str(round(Fahrenheit,2))+'F')
#task 4
timesBatted =1014
notOut = 164
runs = 48426

battingAvg = runs/(timesBatted-notOut)
print('Boycott\'s batting average',round(battingAvg,3))
#task 5
groupSize = 24
studentsOne = 113
studentsTwo = 175
studentsThree = 12
studentOneGroups = studentsOne//groupSize +1
studentOneLeftOver =studentsOne%groupSize
studentTwoGroups = studentsTwo//groupSize +1
studentTwoLeftOver =studentsTwo%groupSize
studentThreeGroups = studentsThree//groupSize +1
studentThreeLeftOver =studentsThree%groupSize

print('with '+str(studentsOne)+' students there will be '+str(studentOneGroups)+' groups and there will be '+str(studentOneLeftOver)+' in the small group')
print('with '+str(studentsTwo)+' students there will be '+str(studentTwoGroups)+' groups and there will be '+str(studentTwoLeftOver)+' in the small group')
print('with '+str(studentsThree)+' students there will be '+str(studentThreeGroups)+' groups and there will be '+str(studentThreeLeftOver)+' in the small group')
