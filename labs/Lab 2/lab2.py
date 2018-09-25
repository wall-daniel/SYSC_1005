# Converts from celsuis to fahrenheit without function
degrees_c = 20.0
degrees_f = degrees_c * 9 / 5 + 32

# Convert imperial to metric fuel consumption
LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

mpg = 32
fuel_consumption_metric = mpg / LITRES_PER_GALLON * KMS_PER_MILE

# Calculate the amount of a certain investment
principle = 1500
rate = 0.043
n = 4
time = 6

amount = principle * (1 + rate/n) ** (n * time)

# Predict the values
a = 2
b = 3
c = 40
d = 4

# Predict the value
x = 3