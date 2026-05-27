import math

y=16.4

print(math.pi)
print(math.e)

result= math.sqrt(y)
print(result)

result= math.ceil(y)
print(result)
result= math.floor(y)
print(result)




#part -2
#circumfarence of circle

radius=float(input(f"enter the radius of circle:"))

circumference= 2* math.pi *radius
print(f"circumfarene of the circle is {circumference}")

#area of circle 


area= round(math.pi * pow(radius,2) ,2)

print(f"area of the circle is {area}")

