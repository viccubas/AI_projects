import numpy as np
import matplotlib.pyplot as plt
import math

NumberOfColumns = 7
NumberOfRows = 200

MinRangeNumber = 0
MaxRangeNumber = 255

NumberOfPoints = 1000
MinimumResolution = 0.2

Weight = 5
BitsInByte = 8


NumberOfChallenges = 5



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
    #plt.pause(10)
        
        
    
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
        
        LocalList = []
        
        Accumulator = 0
        
        #Decode chromosomes into equation parameters
                
        for ChromosomeComponentIndex in range(NumberOfColumns):
            
            LocalList.append(DecodeChromosomes(TargetMatrix[RowIndex, ChromosomeComponentIndex]))
             

        for Index in range(NumberOfPoints):
            
            X = Index / 10
            Accumulator = Accumulator + (abs((OriginalCurveY[Index]) - (LocalList[A_Position] * (LocalList[B_Position] * math.sin(X / LocalList[C_Position]) + (LocalList[D_Position] * math.cos(X / LocalList[E_Position]))) + (LocalList[F_Position] * X) - LocalList[G_Position])))
         
        TargetList.append(Accumulator)
        
    print("Aptitude Function List: ")
    print(TargetList)
    

########################################################################

def DecodeChromosomes(InputValue):
    
    #Avoid division by 0
    
    if(InputValue != 0):
        
        RetVal = InputValue / Weight
        
    else:
        
        RetVal = MinimumResolution
        
    return RetVal

########################################################################


def ApplyTournament(TargetMatrix, ApptitudeResults):
    
    FirstWinnersMatrix = np.zeros([NumberOfRows, NumberOfColumns], dtype=np.uint8)
    SecondWinnerMatrix = np.zeros([NumberOfRows, NumberOfColumns], dtype=np.uint8)
    
    FirstChallengeList = []
    SecondChallengeList = []
    
    TempOriginalMatrix = TargetMatrix
        
    for RowIndex in range(NumberOfRows):
                
        for Index in range(NumberOfChallenges):
            
            #Choose a number of random challengers and store them in a list
            ChallengerIndex1 = np.random.randint(0, NumberOfRows)
        
            FirstChallengeList.append(ApptitudeResults[ChallengerIndex1])
            
            #print("FirstWinner Debug point")
            #print(FirstChallengeList[Index])
            
            ChallengerIndex2 = np.random.randint(0, NumberOfRows)
        
            SecondChallengeList.append(ApptitudeResults[ChallengerIndex2])
            
        #Asign to each winner matrix row the lest accumulated error list index
        FirstWinnersMatrix[RowIndex, 0 : NumberOfColumns] = TempOriginalMatrix[np.argmin(FirstChallengeList), 0 : NumberOfColumns]
        SecondWinnerMatrix[RowIndex, 0 : NumberOfColumns] = TempOriginalMatrix[np.argmin(SecondChallengeList), 0 : NumberOfColumns]
        
        FirstChallengeList.clear()
        SecondChallengeList.clear()
        
        #Operator will produce 2 desecendants from a pair of ancestors
        if((RowIndex % 2) == 0):
            
            ApplyOperator(FirstWinnersMatrix, SecondWinnerMatrix, TargetMatrix, RowIndex)
           
        print(TargetMatrix[RowIndex, 0 : NumberOfColumns])
        
    print(" Descendants generated ")
            
            
            
        


########################################################################

def ApplyOperator(InputMatrix1, InputMatrix2, TargetMatrix, RowIndex):
    
    #From 1 to 55
    RandomSlice =  np.random.randint(1, (BitsInByte * NumberOfColumns))
    DescendantList1 = []
    DescendantList2 = []
        
    BitIndex = 1
    Byte0_Offset = 0
    Byte6_Offset = 0
    
    
    #Determine bit interval
    #Bit 0 - 7
    if(RandomSlice < (1 * BitsInByte)):
        
        ByteIndex = 0
        
        
        if(RandomSlice != ((1 * BitsInByte) - 1)):
            BitIndex = RandomSlice
            
        else:
            #Case in which slice lands on byte separation
            BitIndex = 0
            
            Byte0_Offset = 1
        
    #Bit 8 - 15
    elif(RandomSlice < (2 * BitsInByte)):
        
        ByteIndex = 1
        
        if(RandomSlice != ((2 * BitsInByte) - 1)):
            BitIndex = ((2 * BitsInByte) - 1) - RandomSlice
            
        else:
            #Case in which slice lands on byte separation
            BitIndex = 0
        
    #Bit 16 - 23
    elif(RandomSlice < (3 * BitsInByte)):
        
        ByteIndex = 2
        
        if(RandomSlice != ((3 * BitsInByte) - 1)):
            BitIndex = ((3 * BitsInByte) - 1) - RandomSlice
            
        else:
            #Case in which slice lands on byte separation
            BitIndex = 0
        
    #Bit 24 - 31
    elif(RandomSlice < (4 * BitsInByte)):
        
        ByteIndex = 3
        
        if(RandomSlice != ((4 * BitsInByte) - 1)):
            BitIndex = ((4 * BitsInByte) - 1) - RandomSlice
            
        else:
            #Case in which slice lands on byte separation
            BitIndex = 0
        
    #Bit 32 - 39
    elif(RandomSlice < (5 * BitsInByte)):
        
        ByteIndex = 4
        
        if(RandomSlice != ((5 * BitsInByte) - 1)):
            BitIndex = ((5 * BitsInByte) - 1) - RandomSlice
            
        else:
            #Case in which slice lands on byte separation
            BitIndex = 0
        
    #Bit 40 - 47
    elif(RandomSlice < (6 * BitsInByte)):
        
        ByteIndex = 5
        
        if(RandomSlice != ((6 * BitsInByte) - 1)):
            BitIndex = ((6 * BitsInByte) - 1) - RandomSlice
            
        else:
            #Case in which slice lands on byte separation
            BitIndex = 0
        
    #Bit 48 - 55
    elif(RandomSlice < (7 * BitsInByte)):
        
        ByteIndex = 6
        
        
        if(RandomSlice != ((7 * BitsInByte) - 1)):
            BitIndex = ((7 * BitsInByte) - 1) - RandomSlice
            
            
        else:
            #Case in which slice lands on byte separation
            BitIndex = 0
            
            Byte6_Offset = 1
        
    else:
        
        print("Error : Index out of bounds")
        
        
    #No bitwise separation level
    if(0 == BitIndex):
                
        for Index in range(ByteIndex + 1):
        
            #Find slice separation byte
            if(Index == ByteIndex):
                
                #Byte0_Offset will be a dynamic offset with value 1 if ByteIndex = 0 else offset will be 0.
                #This is needed to ensure that minimum slice value size is [1 : 6]
                xPart = InputMatrix1[RowIndex, 0 : (ByteIndex + Byte0_Offset) - Byte6_Offset]
                yPart = InputMatrix1[RowIndex, ((ByteIndex + 1) - Byte6_Offset) : NumberOfColumns]
                xxPart = InputMatrix2[RowIndex, 0 : (ByteIndex + Byte0_Offset) - Byte6_Offset]
                yyPart = InputMatrix2[RowIndex, ((ByteIndex + 1) - Byte6_Offset) : NumberOfColumns]
                
                print("xPart : {0}, yPart : {1}, xxPart : {2}, yyPart : {3}".format(xPart, yPart, xxPart, yyPart))
                
        #Unpack and append. Order here is important
                
        for CurrentElement in xPart:
        
            DescendantList1.append(CurrentElement)
            
        for CurrentElement in xxPart:
        
            DescendantList2.append(CurrentElement)
            
        for CurrentElement in yPart:
        
            DescendantList2.append(CurrentElement) 
            
        for CurrentElement in yyPart:
        
            DescendantList1.append(CurrentElement)
            
        print("ByteIndex : {0}".format(ByteIndex))
        print("BitIndex : {0}".format(BitIndex))
        print("DescendantList1 : {0}, DescendantList2 : {1}".format(DescendantList1, DescendantList2))
        
        TargetMatrix[RowIndex, 0 : NumberOfColumns] = DescendantList1
        TargetMatrix[RowIndex + 1, 0 : NumberOfColumns] = DescendantList2
        print("TargetMatrix[RowIndex, (0 : NumberOfColumns)] : {0}".format(TargetMatrix[RowIndex, 0 : NumberOfColumns]))
        print("TargetMatrix[RowIndex + 1, (0 : NumberOfColumns)] : {0}".format(TargetMatrix[RowIndex + 1, 0 : NumberOfColumns]))
        
        print("NOT SLICED") 
            
    else:
        
        #Bitwise operator
        
        for Index in range(ByteIndex + 1):
            
            
            if(Index == ByteIndex):
                
                #Boundary value adjustement
                if(0 == ByteIndex):
                    
                    xPart = InputMatrix1[RowIndex, 0 : (ByteIndex + 1)]
                    yPart = InputMatrix1[RowIndex, (ByteIndex + 2) : NumberOfColumns]
                    xxPart = InputMatrix2[RowIndex, 0 : (ByteIndex + 1)]
                    yyPart = InputMatrix2[RowIndex, (ByteIndex + 2) : NumberOfColumns]
                    
                    #If slice is selected on first byte, change to the second one
                    ByteIndex = 1
                    
                elif((NumberOfColumns - 1) == ByteIndex):
                    
                    xPart = InputMatrix1[RowIndex, 0 : (ByteIndex - 1)]
                    yPart = InputMatrix1[RowIndex, ByteIndex : NumberOfColumns]
                    xxPart = InputMatrix2[RowIndex, 0 : (ByteIndex - 1)]
                    yyPart = InputMatrix2[RowIndex, ByteIndex : NumberOfColumns]
                    
                    #If slice is selected on last byte, change selection to the byte before the last one
                    ByteIndex = ByteIndex - 1
                                   
                else:
                    
                    xPart = InputMatrix1[RowIndex, 0 : ByteIndex]
                    yPart = InputMatrix1[RowIndex, (ByteIndex + 1) : NumberOfColumns]
                    xxPart = InputMatrix2[RowIndex, 0 : ByteIndex]
                    yyPart = InputMatrix2[RowIndex, (ByteIndex + 1) : NumberOfColumns]
                                        
                #Retrieve target bytes
                TargetByte1 = InputMatrix1[RowIndex, ByteIndex]
                TargetByte2 = InputMatrix2[RowIndex, ByteIndex]
                
                print("ByteIndex : {0}".format(ByteIndex))
                print("xPart: [{0}] , yPart : [{1}]".format(xPart, yPart))
                print("xxPart: [{0}] ,yyPart : [{1}]".format(xxPart, yyPart))
                

        TargetBytexPart = 0
        TargetByteyPart = 0
        TargetBytexxPart = 0
        TargetByteyyPart = 0
        
        FirstByteMask = 0
        SecondByteMask = 0
        
        print("BitIndex : {0}".format(BitIndex))
        
        for Index in range(BitIndex + 1):
            
            #Apply mask to retrieved bytes
            #Index goes from zero up to bit index slice
            TargetByteyPart = TargetByteyPart | (TargetByte1 & (1 << Index)) 
            TargetByteyyPart = TargetByteyyPart | (TargetByte2 & (1 << Index)) 
            
            #Set bits in variables to apply as masks later on
            FirstByteMask = FirstByteMask | (1 << Index)
            SecondByteMask = SecondByteMask | (1 << Index)
            
        #Clear bits with mask created above
        TargetBytexPart =  TargetByte1 & ~(FirstByteMask)
        TargetBytexxPart = TargetByte2 & ~(SecondByteMask)
        
        print("TargetByteyPart: [{0}] , TargetByteyyPart : [{1}]".format(TargetByteyPart, TargetByteyyPart))    
        print("TargetBytexPart: [{0}] , TargetBytexxPart : [{1}]".format(TargetBytexPart, TargetBytexxPart))
            
        #Concatenate into 2 single bytes
        ResultByte1 = (TargetBytexPart | TargetByteyyPart)
        ResultByte2 = (TargetBytexxPart | TargetByteyPart)
        
        print("ResultByte1 xyy : [{0}] , ResultByte2 xyy : [{1}]".format(ResultByte1, ResultByte2)) 
          

        for CurrentElement in xPart:
         
            DescendantList1.append(CurrentElement)
        
        #Append result byte1 in first vector
        DescendantList1.append(ResultByte1)
            
            
        for CurrentElement in xxPart:
                      
            DescendantList2.append(CurrentElement)
                
        #Append result byte1 in first vector
        DescendantList2.append(ResultByte2)   
            
        for CurrentElement in yPart:
            
            DescendantList2.append(CurrentElement)
                
            
        for CurrentElement in yyPart:
  
            DescendantList1.append(CurrentElement)

                      
        print("** DescendantList1 : {0}, DescendantList2 : {1}".format(DescendantList1, DescendantList2))
        TargetMatrix[RowIndex, 0 : NumberOfColumns] = DescendantList1
        TargetMatrix[RowIndex + 1, 0 : NumberOfColumns] = DescendantList2
        print("** TargetMatrix[RowIndex, (0 : NumberOfColumns)] : {0}".format(TargetMatrix[RowIndex, 0 : NumberOfColumns]))
        print("** TargetMatrix[RowIndex + 1, (0 : NumberOfColumns)] : {0}".format(TargetMatrix[RowIndex + 1, 0 : NumberOfColumns]))
             
        print("SLICED")        
                
                
        
        

########################################################################     

########################################################################

#Create zero matrix of integers
PopulationMatrix = np.zeros([NumberOfRows, NumberOfColumns], dtype=np.uint8)

#Initialize and plot original curve
PlotFirstCurve()

#Initialize random population
InitializePopulation(PopulationMatrix)

#Apply aptitude function and store the result for each row in a list
ApplyAptitudeFunction(PopulationMatrix, AptitudeFunctionResultList)

ApplyTournament(PopulationMatrix, AptitudeFunctionResultList)
    


