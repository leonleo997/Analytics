from sklearn.datasets import load_digits
import pylab as pl
import sklearn.metrics as metrics


def filterValue(digits, value):
    filteredList=[]
    filteredMatrix=[]
    for i in range(0, len(digits.target)-1):
        if digits.target[i]==value:
            filteredList.append(digits.images[i])
    return filteredList

def verifyBlackCol(digit,colIndex):
    isBlack=False
    blackAmount=0
    for i in range(0,8):
        if(digit[i][colIndex]<=3):
            blackAmount+=1
    if blackAmount==8:
        isBlack=True
    return blackAmount

def verifySecondCol(digit):
    answer=False
    amountAproved=0
    for i in range(4,8):
        if(digit[i][1]<4):
            amountAproved+=1
    if amountAproved==4:
        answer=True
    return answer

def verifyThirdCol(digit):
    column=getCol(digit,2)
    answer=False
    #if column[4]==0 or column[5]==0:
    if column[4]<4 or column[5]<4:
        answer=True
    return answer

def verifyFourthCol(digit):
    column=getCol(digit,3)
    answer=False
    #if column[4]==0 or column[5]==0:
    if column[4]<4 or column[5]<4:
        answer=True
    return answer


def verifyFifthCol(digit):
    column=getCol(digit,4)
    answer=False
    count=0
    for i in range(3,7):
        #if(column[i]<=4):
        if(column[i]<=5):
            count+=1
        #delete condition
        #if column[i]==0:
        #    answer=True
    #count > equals to 2
    if(count>=1):
        answer=True
    return answer

def verifySixthCol(digit):
    column=getCol(digit,5)
    answer=False
    count=0
    for i in range(1,len(column)):
        if(column[i]>8):
            count+=1
    #    if(count>=4 and column[0]<5):
    if(count>=4):
        answer=True
    return answer

def verifySeventhCol(digit):
    column=getCol(digit,6)
    answer=False
    count=0
    if column[0]<=4:
        count+=1

    if column[1]<=4:
        count+=1

    if column[2]<=4:
        count+=1

    if column[3]<=4:
        count+=1

    count2=0
    if column[4]>1:
        count2+=1

    if column[5]>1:
        count2+=1

    if column[6]>1:
        count2+=1

    if column[7]>1:
        count2+=1

    #if count>=2 and count2>1:
    if count>=2:
        answer=True

    return answer

def getCol(matrix,col):
    colList=[]
    for i in range(0,8):
        colList.append(matrix[i][col])
    return colList

def isNine(digit):
    answer= True
    if verifyBlackCol(digit,0)==False:
        answer=False
    if verifyBlackCol(digit,7)==False:
        answer=False
    if verifySecondCol(digit)==False:
        answer=False
    if verifyThirdCol(digit)==False:
        answer=False
    if verifyFourthCol(digit)==False:
        answer=False
    if verifyFifthCol(digit)==False:
        answer=False
    if verifySixthCol(digit)==False:
        answer=False
    return answer

digits=load_digits()

realAnswers=[]
for i in range(0,len(digits.target)):
    if(digits.target[i]!=9):
        realAnswers.append(0)
    else:
        realAnswers.append(9)

#x=[]
#for val in filteredList:
    #columna=getCol(val,5)
    #pl.matshow(columna)
    #if(columna[0]>4):
    #print("{0} {1} {2} {3}".format(columna[4],columna[5],columna[6],columna[7]))

predictedAnswers=[]
for val in digits.images:
    if isNine(val)==True:
        #print(val)
        predictedAnswers.append(9)
    else:
        predictedAnswers.append(0)
        #columna=getCol(val,4)
        #print("{0} {1} {2} {3}".format(columna[3],columna[4],columna[5],columna[6]))

print("The accuracy is: "+str(metrics.accuracy_score(realAnswers, predictedAnswers)*100)+" %")
print("Predicted:   "+str(predictedAnswers[0:30]))
print("Target:      "+str(realAnswers[0:30]))

#pl.matshow(filteredList[1])
#pl.matshow(filteredList[2])
#pl.matshow(filteredList[3])
#pl.matshow(filteredList[4])
#pl.matshow(filteredList[5])
