import matplotlib.pyplot as plt
import numpy as np


def InputABC():
    a = input("pls enter A: ")
    b = input("pls enter B: ")
    c = input("pls enter C: ")
    return int(a), int(b), int(c)

def PrintP(a, b, c):
    x = np.linspace(0, 100, 1000)
    y = a*x**2 + b*x + c
    plt.plot(x, y)
   
def ListPoints():
    matrix = np.array([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])
    for i in range (10):
        matrix[i] [0] = int(input("pls enter X value: "))
        matrix[i] [1] = int(input("pls enter Y value: "))
    return matrix

def DistanceB(a, b, c, points):
    x = 0  #מכיל את מספר הנקודות שלא על הפרבולה
    distance = 0  #מכיל את המרחק בין כל הנקודות לבין הפרבולה
    for i in range (10):
        distance += np.abs(a*points[i][0]**2 + b*points[i][0] + c - points[i][1])
        if not (distance == distance):
            x +=1
    return x, distance  
   
def main():
    bestX = 10  #ייכיל את מספר הנקודות הקרובות ביותר לשלמות
    for i in range (50):
        a, b, c = InputABC() 
        x, d = DistanceB(a, b, c, ListPoints())  #x = למספר הנקודות שלא על הפרבולה    d = לסכום המרחקים של הנקודות מהפרבולה
        if x == 0 and d == 0:
            bestA = a
            bestB = b
            bestC = c
            break #יבצע ברייק
        elif bestX > x:
            bestA = a
            bestB = b
            bestC = c
    print (bestA, bestB, bestC)
main()       
        