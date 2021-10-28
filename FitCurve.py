import numpy as np
import matplotlib.pyplot as plt
import math

A = 8
B = 25
C = 4
D = 45
E = 10
F = 17
G = 35

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))

FirstCurveX = []
FirstCurveY = []

########################################################################

def PlotFirstCurve():
    
        
    for Index in range(1000):        
        X = Index / 10
        Y = A * (B * math.sin(X / C) + (D * math.cos(X / E))) + (F * X) - G
        
        print("X : {0} ".format(X))
        print("Y : {0} ".format(Y))
            
        FirstCurveX.append(X)
        FirstCurveY.append(Y)
            
    # Plot first curve
    axes.clear()
    axes.plot(FirstCurveX, FirstCurveY)
    
    fig.show()
    plt.pause(10)
        
        
    
########################################################################



PlotFirstCurve()

