import numpy as np
import matplotlib.pyplot as plt
import math

NumberOfColumns = 7
NumberOfRows = 200

MinRangeNumber = 0
MaxRangeNumber = 255

NumberOfPoints = 1000

Weight = 5

A = 8
B = 25
C = 4
D = 45
E = 10
F = 17
G = 35

A_Position = 0
B_Position = 1
C_Position = 2
D_Position = 3
E_Position = 4
F_Position = 5
G_Position = 6

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))

OriginalCurveX = []
OriginalCurveY = []

AptitudeFunctionResultList = []

########################################################################

def PlotFirstCurve():
    
        
    for Index in range(NumberOfPoints):        
        X = Index / 10
        Y = A * (B * math.sin(X / C) + (D * math.cos(X / E))) + (F * X) - G
        
        #print("X : {0} ".format(X))
        #print("Y : {0} ".format(Y))
            
        OriginalCurveX.append(X)
        OriginalCurveY.append(Y)
            
    # Plot first curve
    axes.clear()
    axes.plot(OriginalCurveX, OriginalCurveY)
    
    fig.show()
    plt.pause(10)
        
        
    
########################################################################

def InitializePopulation(InitMatrix):
    
    print("Initialize population")
    
    for RowIndex in range(NumberOfRows):
    
        for ColumnIndex in range(NumberOfColumns):
        
            InitMatrix[RowIndex, ColumnIndex] = np.random.randint(MinRangeNumber, (MaxRangeNumber + 1))
    
        print(InitMatrix[RowIndex, 0 : NumberOfColumns])
    


########################################################################

def ApplyAptitudeFunction(TargetMatrix, TargetList):
    
    for RowIndex in range(NumberOfRows):
        
        Accumulator = 0
        
        #Decode chromosomes into equation parameters
        
        #Check to avoid division by 0
        if(TargetMatrix[RowIndex, A_Position] < Weight):
            A_local = 0.2
        else:
            A_local = (TargetMatrix[RowIndex, A_Position] / Weight)
            
        if(TargetMatrix[RowIndex, B_Position] < Weight):
            B_local = 0.2
        else:
            B_local = (TargetMatrix[RowIndex, B_Position] / Weight)
            
        if(TargetMatrix[RowIndex, C_Position] < Weight):
            C_local = 0.2
        else:
            C_local = (TargetMatrix[RowIndex, C_Position] / Weight)
            
        if(TargetMatrix[RowIndex, D_Position] < Weight):
            D_local = 0.2
        else:
            D_local = (TargetMatrix[RowIndex, D_Position] / Weight)
            
        if(TargetMatrix[RowIndex, E_Position] < Weight):
            E_local = 0.2
        else:
            E_local = (TargetMatrix[RowIndex, E_Position] / Weight)
            
        if(TargetMatrix[RowIndex, F_Position] < Weight):
            F_local = 0.2
        else:
            F_local = (TargetMatrix[RowIndex, F_Position] / Weight)
            
        if(TargetMatrix[RowIndex, G_Position] < Weight):
            G_local = 0.2
        else:
            G_local = (TargetMatrix[RowIndex, G_Position] / Weight)
        
        
        for Index in range(NumberOfPoints):
            
            X = Index / 10
            Accumulator = Accumulator + (abs((OriginalCurveY[Index]) - (A_local * (B_local * math.sin(X / C_local) + (D * math.cos(X / E_local))) + (F_local * X) - G_local)))
         
        TargetList.append(Accumulator)
        
    print("Aptitude Function List: ")
    print(TargetList)
    

########################################################################

#Create zero matrix of integers
PopulationMatrix = np.zeros([NumberOfRows, NumberOfColumns], dtype=np.uint8)

#Initialize and plot original curve
PlotFirstCurve()

#Initialize random population
InitializePopulation(PopulationMatrix)

#Apply aptitude function and store the result for each row in a list
ApplyAptitudeFunction(PopulationMatrix, AptitudeFunctionResultList)
    


