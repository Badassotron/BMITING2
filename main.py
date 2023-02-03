import random

name = input('Whats your name?')
print('Hello', name.capitalize())

print('ok then')
weight = float(input('Whats your weight in Kg?'))
height = float(input('How tall are you in Cm?'))
BMI = weight/(height/100)**2
print('your BMI is', {BMI})

n= random.randint(1,365)
a= random.randint(1,24)
print('therefore your balls will explode in')
print('calculating......')
print(n,'days and',a,'hours')