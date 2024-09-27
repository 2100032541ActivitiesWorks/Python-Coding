print("Speed Calculation")
print("=====================")
def speed(a, b):
    print("The Speed of the Object is: ",a / b,"km/hrs")
    
x = int(input("Enter the Distance: "))
print("The distance is: ",x,"Km")
y = int(input("Enter the time: "))
print("The Time taken is:",y,"hrs")

speed(x, y)

print()
print("Distance Calculation")
print("=====================")
def distance(c, d):
    print("The Distance covered by the object is: ",c * d,"km")
    
x = int(input("Enter the speed: "))
print("The Speed of object is:",x,"km/hrs")
y = int(input("Enter the time: "))
print("The Time taken is:",y,"hrs")

distance(x, y)

print()
print("Time Calculation")
print("=====================")
def time(e, f):
    print("The Time taken by the object is: ",e / f,"hrs")
    
x = int(input("Enter the Distance: "))
print("The distance is: ",x,"Km")
y = int(input("Enter the speed: "))
print("The Speed of object is:",x,"km/hrs")

time(x, y)
