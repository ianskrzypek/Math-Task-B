import math
#These are the functions which find the surface areas, volumes, areas, and perimeters
def acircle(x):
    return math.pi*x**2
def pcircle(x):
    return math.pi*x*2
def vcyclinder(x,y=10):
    return math.pi*x**2*y
def sacyclinder(x,y=10):
    return 2*math.pi*(x**2+x*y)
def vsphere(x):
    return 4/3*math.pi*x**3
def sasphere(x):
    return 4*math.pi*radius**2
def vcone(x,y=10):
    return math.pi*x**2*y/3
def sacone(x,y=10):
    return math.pi*x*(x+math.sqrt(y**2+x**2))
#the below function allows me to use and print the result of the above functions while wasting less code 
def run(x,y,z,w,q):
    y = x(y)
    print ("The",z,"of your",w,"with a radius of",radius,"cm is",y,q)
#the code below allows the user to enter a radius, and will check if the input is actually a number,
#and if it is above zero, as a shape cannot have a negative side length. It will repeat until all conditions are met
step1 = ("false")
while step1 == "false":
    try:
        radius = float(input("enter a radius for your shapes (in cm): "))
        if radius <= 0:
            print("your number must be greater than zero")
        else:
            step1 = "true"
    except ValueError:
        print("you must only enter a number")
#the code below activates and combines all previous functions
run(acircle,radius,"area","circle","cm2")
run(pcircle,radius,"perimeter","circle","cm")
run(vcyclinder,radius,"volume","cyclinder","cm3")
run(sacyclinder,radius,"surface area","cylilnder","cm2")
run(vsphere,radius,"volume","sphere","cm3")
run(sasphere,radius,"surface area","sphere","cm2")
run(vcone,radius,"volume","cone","cm3")
run(sacone,radius,"surface area","cone","cm2")