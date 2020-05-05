#Write a Python program to find the volume of a sphere with diameter 12 cm.
#Formula: V=4/3 * π * r 3

import math

def volume(r):
   Volume = (4/3)*(math.pi)*math.pow(r,3)
   return Volume

def main():
   radius = float(input("Enter the radius of the sphere:"))
   v=volume(radius)
   print(v)

if __name__=="__main__":
   main()
