import numpy as np
import matplotlib.pyplot as plt
import math

NumberOfColumns = 20
NumberOfRows = 300

MinRangeNumber = 1
MaxRangeNumber = 20

NumberOfChallengedIndividuals = 15

NumberOfGenerations = 300

NumberOfReproductionOperators = 2
FirstReproductionOperator = 0
SecondReproductionOperator = 1

MaxXCoordinate = 13
MaxYCoordinate = 8

#Coordinates
XPosition = 0
YPosition = 1
 
City1 = (1, 6)
City2 = (1, 4)
City3 = (2, 8)
City4 = (2, 3)
City5 = (2, 1)
City6 = (3, 6)
City7 = (4, 3)
City8 = (4, 1)
City9 = (5, 7)
City10 = (6, 2)

City11 = (7, 8)
City12 = (7, 4)
City13 = (8, 6)
City14 = (8, 3)
City15 = (9, 2)
City16 = (10, 7)
City17 = (11, 6)
City18 = (11, 1)
City19 = (12, 3)
City20 = (13, 5)

CitiesCoordinates = (City1,  City2,  City3,  City4,  City5,
                     City6,  City7,  City8,  City9,  City10,
                     City11, City12, City13, City14, City15,
                     City16, City17, City18, City19, City20)
                     

############################################################################################

def FillRow(CurrentRow, TargetMatrix):
#List to check whether a number is already in use and avoid repetition    
    NumberCheckList = [False, False, False, False, False,
                       False, False, False, False, False,
                       False, False, False, False, False,
                       False, False, False, False, False]
    
    for ColumnIndex in range(NumberOfColumns):
       
        #Get random number between MinRangeNumber and MaxRangeNumber
        CurrentRandomDigit = np.random.randint(MinRangeNumber, (MaxRangeNumber + 1))
        #Number is already used in this row
        while(True == NumberCheckList[CurrentRandomDigit - 1]):
            #Loop until get an unused random number
            CurrentRandomDigit = np.random.randint(MinRangeNumber, (MaxRangeNumber + 1))
        #Mark digit as used 
        NumberCheckList[CurrentRandomDigit - 1] = True
        #Fill matrix member with selected random number
        TargetMatrix[CurrentRow, ColumnIndex] = CurrentRandomDigit    
        
############################################################################################
def InitializePopulation(InitMatrix):
    
    print("Initial Population:")
    
    for RowIndex in range(NumberOfRows):
        #Fill all rows with random values
        FillRow(RowIndex, InitMatrix)
        print(InitMatrix[RowIndex, MinRangeNumber - 1 : MaxRangeNumber])
        
    print(" ")
    print(" ")
    print(" ")        
    
############################################################################################
def ApplyAptitudeFunction(TargetAptitudeResultList, TargetMatrix):
    
    #Clear list before doing any operation
    TargetAptitudeResultList.clear()
    
    for RowIndex in range(NumberOfRows):
        Accumulator = 0
    
        #Substract a one because of each of operation number
        for ColumnIndex in range(NumberOfColumns - 1):
            #Get Pivot cities from population matrix
            Pivot1 = TargetMatrix[RowIndex, ColumnIndex]
            Pivot2 = TargetMatrix[RowIndex, ColumnIndex + 1]
            #Use pivots ID as index for coordinates tuple
            DistanceinX = CitiesCoordinates[Pivot1 - 1][XPosition] - CitiesCoordinates[Pivot2 - 1][XPosition]
            DistanceinY = CitiesCoordinates[Pivot1 - 1][YPosition] - CitiesCoordinates[Pivot2 - 1][YPosition]
            #Calculate distances from given points
            DistanceInBet = math.sqrt(((DistanceinX ** 2) + (DistanceinY ** 2)))
            #Sum up
            Accumulator = Accumulator + DistanceInBet
    
        TargetAptitudeResultList.append(Accumulator)

        

############################################################################################
def GetWinnersVector(TargetWinnersVector, TargetAptitudeResultList):

    #Clear list before doing any operation
    TargetWinnersVector.clear()
    
    for Index in range(NumberOfRows):
        #Perform challenge
        WinnerIndiv = PerformChallenge(TargetAptitudeResultList)
        #Append winner individual to the list
        TargetWinnersVector.append(WinnerIndiv)
        

############################################################################################
def PerformChallenge(TargetAptitudeResultList):
    
    SelectedIndividualsList = []
    WinnersIndividualsList = []

    for Index in range(NumberOfChallengedIndividuals):
        #Select random individual
        CurrentRandomDigit = np.random.randint(0, NumberOfRows)
        WinnersIndividualsList.append(CurrentRandomDigit)
        #Fill list with distances 
        SelectedIndividualsList.append(TargetAptitudeResultList[CurrentRandomDigit])

    #Select winner
    #return index of lowest value in list
    return WinnersIndividualsList[np.argmin(SelectedIndividualsList)]
        

############################################################################################
def MapVectorToMatrix(TargetWinnersVector, TargetMatrix):
    
    #Make a copy of target matrix
    TempMatrix = TargetMatrix
    
    for Index in range(NumberOfRows):
        TargetMatrix[Index, 0 : NumberOfColumns] = TempMatrix[(TargetWinnersVector[Index]), 0 : NumberOfColumns]
        
    #print(PopulationMatrix)
    #print("Winners Matrix: ")
    #for Index in range(NumberOfRows):
        #print(PopulationMatrix[Index, MinRangeNumber - 1 : MaxRangeNumber])
        
        
############################################################################################

def ReproductionOperator1(TargetMatrix, CurrentRow):
    #Initialize random variables
    RandomPoint1 = np.random.randint(0, NumberOfColumns)
    RandomPoint2 = np.random.randint(0, NumberOfColumns)
    RandomLength = np.random.randint(1, (NumberOfColumns / 2))
    
    IsPoint2Greater = False
    
    ResultVector = []
    FlatVector = []
    
    
    CurrentVector = TargetMatrix[CurrentRow,  0 : NumberOfColumns]
    
    print("Original : ")
    print(CurrentVector)
     
    
    #Make sure that we get different points
    while(RandomPoint1 == RandomPoint2):
            RandomPoint2 = np.random.randint(0, NumberOfColumns)
            
    #print("RandomLength")
    #print(RandomLength)
    #print("RandomPoint1")
    #print(RandomPoint1)
    #print("RandomPoint2")
    #print(RandomPoint2)
            
    
    if(RandomPoint2 > RandomPoint1):
        IsPoint2Greater = True
        #Check the distance between points to avoid overlapping
        if((RandomPoint2 - RandomPoint1) <= RandomLength):
            
            RandomPoint1 = RandomPoint2 - (RandomLength + 1)
            
            if(RandomPoint1 < 0):
                RandomPoint1 = NumberOfColumns - abs(RandomPoint1)
                IsPoint2Greater = False
    else:
        IsPoint2Greater = False
        
        #Check the distance between points to avoid overlapping
        if((RandomPoint1 - RandomPoint2) <= RandomLength):
            
            RandomPoint2 = RandomPoint1 - (RandomLength + 1)
            if(RandomPoint2 < 0):
                RandomPoint2 = NumberOfColumns - abs(RandomPoint2)
                IsPoint2Greater = True
            
    
    if((RandomPoint1 + RandomLength) > NumberOfColumns):
        Point1Remainder = ((RandomPoint1 + RandomLength) - NumberOfColumns)
        
        if(Point1Remainder >= RandomPoint2):
            RandomPoint2 = RandomPoint2 + Point1Remainder
            
            #Case in which recalculated point2 plus length overlaps point1
            if((RandomPoint2 + RandomLength)  > RandomPoint1):
                RandomPoint2 = RandomPoint2 - ((RandomPoint2 + RandomLength) - RandomPoint1)
            elif((RandomPoint2 + RandomLength) == RandomPoint1):
                RandomPoint2 = RandomPoint2 - 1
            
    else:
        Point1Remainder = 0
        
    if((RandomPoint2 + RandomLength) > NumberOfColumns):
        Point2Remainder = ((RandomPoint2 + RandomLength) - NumberOfColumns)
        
        if(Point2Remainder >= RandomPoint1):
            RandomPoint1 = RandomPoint1 + Point2Remainder
            
            #Case in which recalculated point1 plus length overlaps point2
            if((RandomPoint1 + RandomLength)  > RandomPoint2):
                RandomPoint1 = RandomPoint1 - ((RandomPoint1 + RandomLength) - RandomPoint2)
            elif((RandomPoint1 + RandomLength) == RandomPoint2):
                RandomPoint1 = RandomPoint1 - 1
            
    else:
        Point2Remainder = 0
        
        
    if(Point1Remainder > 0):
     
        ResultVector.append(CurrentVector[0 : Point1Remainder])
        ResultVector.append(CurrentVector[Point1Remainder : RandomPoint2])
        ResultVector.append(CurrentVector[RandomPoint2 : (RandomPoint2 + RandomLength)])
        ResultVector.append(CurrentVector[(RandomPoint2 + RandomLength) : RandomPoint1])
        ResultVector.append(CurrentVector[RandomPoint1 : NumberOfColumns])
        
        OverlapConcat = [*ResultVector[4], *ResultVector[0]]
        
        FlatVector = [*ResultVector[2], *ResultVector[1], *OverlapConcat, *ResultVector[3]]
                   
    elif(Point2Remainder > 0):
 
        ResultVector.append(CurrentVector[0 : Point2Remainder])
        ResultVector.append(CurrentVector[Point2Remainder : RandomPoint1])
        ResultVector.append(CurrentVector[RandomPoint1 : (RandomPoint1 + RandomLength)])
        ResultVector.append(CurrentVector[(RandomPoint1 + RandomLength) : RandomPoint2])
        ResultVector.append(CurrentVector[RandomPoint2 : NumberOfColumns])
        
        OverlapConcat = [*ResultVector[4], *ResultVector[0]]
        
        FlatVector = [*ResultVector[2], *ResultVector[1], *OverlapConcat, *ResultVector[3]]
           
    else:
        
        if(True == IsPoint2Greater):
            
            ResultVector.append(CurrentVector[0 : RandomPoint1])
            ResultVector.append(CurrentVector[RandomPoint1 : (RandomPoint1 + RandomLength)])
            ResultVector.append(CurrentVector[(RandomPoint1 + RandomLength) : (RandomPoint2)])
            ResultVector.append(CurrentVector[RandomPoint2 : (RandomPoint2 + RandomLength)])
            ResultVector.append(CurrentVector[(RandomPoint2 + RandomLength) : NumberOfColumns])
            #Unpacking operator
            FlatVector = [*ResultVector[0], *ResultVector[3], *ResultVector[2], *ResultVector[1], *ResultVector[4]]
       
        else:
            ResultVector.append(CurrentVector[0 : RandomPoint2])
            ResultVector.append(CurrentVector[RandomPoint2 : (RandomPoint2 + RandomLength)])
            ResultVector.append(CurrentVector[(RandomPoint2 + RandomLength) : (RandomPoint1)])
            ResultVector.append(CurrentVector[RandomPoint1 : (RandomPoint1 + RandomLength)])
            ResultVector.append(CurrentVector[(RandomPoint1 + RandomLength) : NumberOfColumns])
            
            FlatVector = [*ResultVector[0], *ResultVector[3], *ResultVector[2], *ResultVector[1], *ResultVector[4]]
            
    
    #print("RandomLength")
    #print(RandomLength)
    #print("RandomPoint1")
    #print(RandomPoint1)
    #print("RandomPoint2")
    #print(RandomPoint2)
    #print("Point1Remainder")
    #print(Point1Remainder)
    #print("Point2Remainder")
    #print(Point2Remainder)
            
    #for Index in range(5):
        #print(ResultVector[Index])
        
    
    TargetMatrix[CurrentRow,  0 : NumberOfColumns] = FlatVector
    
    print(TargetMatrix[CurrentRow,  0 : NumberOfColumns])
        
        

############################################################################################

def ReproductionOperator2(TargetMatrix, CurrentRow):
    #Initialize random variables
    RandomPoint = np.random.randint(0, NumberOfColumns)
    RandomLength = np.random.randint(2, NumberOfColumns)
    
    #print("RandomLength")
    #print(RandomLength)
    #print("RandomPoint")
    #print(RandomPoint)
    
    ResultVector = []
    FlatVector = []
    
    CurrentVector = TargetMatrix[CurrentRow,  0 : NumberOfColumns]
    
    print("Original : ")
    print(CurrentVector)
    
    if((RandomPoint + RandomLength) > NumberOfColumns):
        PointRemainder = ((RandomPoint + RandomLength) - NumberOfColumns)
    else:
        PointRemainder = 0
        
    #print("PointRemainder")
    #print(PointRemainder)
        
        
    if(PointRemainder > 0):
     
        ResultVector.append(CurrentVector[0 : PointRemainder])
        ResultVector.append(CurrentVector[PointRemainder : RandomPoint])
        ResultVector.append(CurrentVector[RandomPoint : NumberOfColumns])
        
        ResultVector[0] = np.flip(ResultVector[0])
        ResultVector[2] = np.flip(ResultVector[2])
        
        FlatVector = [*ResultVector[0], *ResultVector[1], *ResultVector[2]]
                   
    else:
        ResultVector.append(CurrentVector[0 : RandomPoint])
        ResultVector.append(CurrentVector[RandomPoint : (RandomPoint + RandomLength)])
        ResultVector.append(CurrentVector[(RandomPoint + RandomLength) : NumberOfColumns])
        #Reverse selected slice
        ResultVector[1] = np.flip(ResultVector[1])
        
        FlatVector = [*ResultVector[0], *ResultVector[1], *ResultVector[2]]
        
        
    TargetMatrix[CurrentRow,  0 : NumberOfColumns] = FlatVector
        
    print(TargetMatrix[CurrentRow,  0 : NumberOfColumns])
    
 
############################################################################################

def ApplyReproductionOperator(TargetMatrix, CurrentRow):
    #Initialize random variables
    FlipCoin = np.random.randint(0, NumberOfReproductionOperators)
    
    #print("Result of Flip")
    #print(FlipCoin)
   
    if(FlipCoin == FirstReproductionOperator):
       ReproductionOperator1(TargetMatrix, CurrentRow)   
    else:
       ReproductionOperator2(TargetMatrix, CurrentRow)
       

############################################################################################

def PlotBestDistance(TargetDistanceList, Generation):
   
    print("Generation : {0}".format(Generation + 1))
    print("Shortest distance in generation : {0}".format(min(TargetDistanceList)))
    
    X_CityList = []
    Y_CityList = []
    X_BestTripSoFarList = []
    Y_BestTripSoFarList = []
    
    #Collect shortest distance and append it to a list
    gBestDistanceList.append(min(TargetDistanceList))
    TripIndex = np.argmin(gBestDistanceList)
    
    
    gBestTripList.append(PopulationMatrix[TripIndex][0 : MaxRangeNumber])
    print("Last Best Trip : {0}".format(gBestTripList[-1]))
    
    axes[0].set_title("Shortest distance")
    axes[0].set_ylabel("Best distance in generation")
    axes[0].set_xlabel("Generation")
    
    axes[1].set_title("Best trip in generation")
    axes[1].set_ylabel("Y City Coordinate")
    axes[1].set_xlabel("X City Coordinate")
    
    axes[2].set_title("Best trip so far")
    axes[2].set_ylabel("Y City Coordinate")
    axes[2].set_xlabel("X City Coordinate")
    
    # Plot Generation Against Shortest distance
    axes[0].clear()
    axes[0].plot(list(range(0 , Generation + 1)), gBestDistanceList)
    
    #Unpack corresponding city coordinates of last best trip and append them in corresponding list
    for CityIndex in gBestTripList[-1]:
        X_CityList.append(CitiesCoordinates[CityIndex - 1][0])
        Y_CityList.append(CitiesCoordinates[CityIndex - 1][1])
        
    gX_BestTripSoFarList.append(X_CityList)
    gY_BestTripSoFarList.append(Y_CityList)
    
        
    #Plot coordinates    
    axes[1].clear()
    axes[1].plot(X_CityList, Y_CityList)
    
    for CityIndex in gX_BestTripSoFarList[TripIndex]:
        X_BestTripSoFarList.append(CityIndex)
        
    for CityIndex in gY_BestTripSoFarList[TripIndex]:
        Y_BestTripSoFarList.append(CityIndex)
        
    #Plot coordinates    
    axes[2].clear()
    axes[2].plot(X_BestTripSoFarList, Y_BestTripSoFarList)
    
    print("Best distance so far : {0}".format(min(gBestDistanceList)))

    fig.show()
    plt.pause(0.02)
        

############################################################################################
#Create zero matrix of integers
PopulationMatrix = np.zeros([NumberOfRows, NumberOfColumns], dtype=np.int8)
#Create empty list for aptitude result vector
AptitudeResultVector = []
WinnersVector = []
gBestDistanceList = []
gBestTripList = []
gX_BestTripSoFarList = []
gY_BestTripSoFarList = []

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 5))


#Fill matrix with initial population
InitializePopulation(PopulationMatrix)

ApplyAptitudeFunction(AptitudeResultVector, PopulationMatrix)

GetWinnersVector(WinnersVector, AptitudeResultVector)

MapVectorToMatrix(WinnersVector, PopulationMatrix)
    
for GenerationIndex in range(NumberOfGenerations):
    
    #Apply a reproduction operator to each row in matrix
    for RowIndex in range(NumberOfRows):
        ApplyReproductionOperator(PopulationMatrix, RowIndex)
    
    for ShowRow in range(NumberOfRows):
        print(PopulationMatrix[ShowRow, 0 : NumberOfColumns])
        
    PlotBestDistance(AptitudeResultVector, GenerationIndex)
               
    ApplyAptitudeFunction(AptitudeResultVector, PopulationMatrix)

    GetWinnersVector(WinnersVector, AptitudeResultVector)

    MapVectorToMatrix(WinnersVector, PopulationMatrix)
    


        








