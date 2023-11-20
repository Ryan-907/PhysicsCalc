import pyinputplus as pyin
from Kinematics import *
if __name__ == '__main__':
    print("Welcome to my physics calculator please choose one of the following:")
    print("1-Calculate force")
    choice = int(input())

    if choice == 1:
        mass = pyin.inputFloat("Pleas enter mass (if unknown, enter 0)")
        acceleration = pyin.inputFloat("Pleas enter acceleration (if unknown, enter 0)")
        force = pyin.inputFloat("Pleas enter force (if unknown, enter 0)")
        print(Force(force, mass, acceleration)) 