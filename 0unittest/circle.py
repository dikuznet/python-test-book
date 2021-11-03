from math import pi

def ca(radius):
    if type(radius) not in [int,float]: 
        raise TypeError("Type not compartable")       
    if radius < 0:
        raise ValueError("Radius can't be negative")
    return pi*radius**2

if __name__=="__main__":
    print(ca(-1))