import random

name = input('Whats your name?')
print('Hello', name.capitalize())

print('ok then')
weight = (input('Whats your weight in Kg?' ))
height = (input('How tall are you in Cm?' ))
if "," in weight:
    temp = weight.split(",")
    print(temp)
    weight = temp[0] + "." + temp[1]
BMI = float(weight)/(float(height)/100)**2
print('your BMI is', {BMI})

n= random.randint(1,365)
a= random.randint(1,24)
print('therefore your balls will explode in')
print('calculating......')
print(n,'days and',a,'hours')