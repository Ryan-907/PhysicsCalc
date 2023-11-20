from Kinematics import *
from material import * 

#This ensures anything is either a float or a None. 
def to_float(x):
    try:
        x = float(x)
        return x
    except ValueError:
        return ''
    
if __name__ == '__main__':

    #Greeting :)
    print("Welcome to my physics calculator please choose one of the following:")
    print("First lets make an item to experience physics. Leave blank any unknown variables. ")
    
    #Taking details about the item. I usually name my item Tim :)
    n = input("Objects name is: ")
    f = to_float(input("Force: "))
    m = to_float(input("Mass: "))
    a = to_float(input("Acceleration: "))
    w = to_float(input("Weight: "))
    d = to_float(input("Distance: "))
    t = to_float(input("Time: "))
    W = to_float(input("Work done: "))

    #Initializing the Data Class
    item = material(name=n, force=f, mass = m,acceleration=a, weight=w, distance=d, time=t, work=w)

    #Checks if force is known. If not, it assigns force to the result. There has to be a better way so I can get
    #a good print out. That will prob be besy fixed when I make a GUI.
    if item.force:
        print(f'{item.name} {Force(item.force, item.mass, item.acceleration)}')
    else:
        print(f'{item.name} {Force(item.force, item.mass, item.acceleration)}')
        item.force = Force(item.force, item.mass, item.acceleration)

    print(f'{item.name} {Work(item.work, item.force, item.distance)}')