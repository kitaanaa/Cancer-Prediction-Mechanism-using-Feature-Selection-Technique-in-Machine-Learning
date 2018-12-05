import xlrd
import sys
import numpy
import time
from math import *

#################################### COST FUNCTION##########################
def distanceCal(comb1):
    #print(comb1)imp
    temp=0
    comb1=comb1
    #print(comb1)imp
    firstListCpy=[]
    secondListCpy=[]
    bigListCpy1=[]

    ######################### TAKING SELECTED FEATURES################################
    for x in range(len(bigListCpy)):
        smallListCpy1=[]
        for y in range(len(firstList[0])):
            if(int(comb1[y])):
                smallListCpy1.append(bigListCpy[x][y])
        bigListCpy1.append(smallListCpy1)
        if(x<len(bigListCpy)/2):
            firstListCpy.append(smallListCpy1)
        else:
            secondListCpy.append(smallListCpy1)
    # # print(bigListCpy1,flush=True)
    # print(firstListCpy,flush=True)
    # print(secondListCpy,flush=True)
    ##########################LIST1############################
    for y in range(len(firstListCpy[0])):
        pointList1.append(firstListCpy[0][y])

    for z in range(len(bigListCpy1)):
        for v in range(len(bigListCpy1[z])):
            pointList2.append(bigListCpy1[z][v])

        ##########################DISTANCE FORMULA############################
        for i in range(len(pointList1)):
            temp+=(float(pointList2[i])-float(pointList1[i]))**2
            # print(temp,flush=True)

        distanceList1.append(int(sqrt(temp)))
        temp=0
        # print(pointList2,flush=True)
        pointList2.clear()

    # print(pointList1,flush=True)
    pointList1.clear()
    # print(distanceList1,flush=True)

    ##########################LIST2############################
    for y in range(len(secondListCpy[0])):
        pointList1.append(secondListCpy[0][y])

    for z in range(len(bigListCpy1)):
        for v in range(len(bigListCpy1[z])):
            pointList2.append(bigListCpy1[z][v])

        ##########################DISTANCE FORMULA############################
        for i in range(len(pointList1)):
            temp+=(float(pointList2[i])-float(pointList1[i]))**2
            # print(temp,flush=True)

        distanceList2.append(int(sqrt(temp)))
        temp=0
        # print(pointList2,flush=True)
        pointList2.clear()

    # print(pointList1,flush=True)
    pointList1.clear()
    # print(distanceList2,flush=True)


    # print("distList1",distanceList1,flush=True)
    # print("distList2",distanceList2,flush=True)

    cost=0
    for k in range(len(distanceList1)):
        if(distanceList1[k]>distanceList2[k]):
            classList.append(0)
        else:
            classList.append(1)
    y=0
    # print(classList)
    ########################## COMPARISON ########################################
    for x in range(1,len(bigList)):
        # print(bigList)
        if(int(classList[y])==int(bigList[x][-1])):
            cost+=1
        y+=1
    cost=float(1/cost)
    # print(comb1)
    # print(cost,flush=True)
    classList.clear()
    distCost.append(cost)


######################## EXTRA FUNCTIONS ###########################################
def findMean(l1):
    mean=0
    for v in l1:
        mean+=v
    mean/=(len(l1))
    return mean

def findAvg(l1):
    mean=0
    for v in l1:
        mean+=v
    mean/=(len(l1))
    return mean*0.13

def findCoef(xlist,mean):
    percentage=[]
    for i in xlist:
        percentage.append(i/mean)
    return percentage

############################ EQUATION FUNC#####################
def findGroup(l1,coef,zeroconstant,l2,coef1,oneconstant):
    zero_val=0
    one_val=0

    for i in range(len(l1)):
        zero_val+=(l1[i]*coef[i])
    zero_val+=zeroconstant
    for i in range(len(l2)):
        one_val+=(l2[i]*coef1[i])
    one_val+=oneconstant
    ########################HYPER PLANE####################
    return findAvg([zero_val,one_val])


##################################FINDING HYPER PLANE###################################
def calculateSVM(comb):
    oneList=[]
    zeroList=[]
    mean=[]
    variance=[]
    sd=[]
    skewness=[]
    kurtosis=[]
    mean1=[]
    variance1=[]
    sd1=[]
    skewness1=[]
    kurtosis1=[]
    bigListCpy1=[]

    comb+='1'
    # print(comb)
    z=0
    for x in range(len(bigList)):
        smallListCpy1=[]
        for y in range(1,len(bigList[0])):
            if(int(comb[y-1])):
                smallListCpy1.append(bigList[x][y])

        bigListCpy1.append(smallListCpy1)
    # print(bigListCpy1)

    # bigListCpy1=bigList.copy()


    for i in range(1,len(bigListCpy1)):
        if(bigListCpy1[i][-1]==1):
            oneList.append(bigListCpy1[i])
            # oneList[-1].pop(0)
            oneList[-1].pop(-1)
        else:
            zeroList.append(bigListCpy1[i])
            # zeroList[-1].pop(0)
            zeroList[-1].pop(-1)
    # print(zeroList)
    # print(oneList)
    zeroFeature1Mean=findMean(zeroList[0])
    zeroFeature2Mean=findMean(zeroList[1])
    zeroFeature3Mean=findMean(zeroList[2])
    oneFeature1Mean=findMean(oneList[0])
    oneFeature2Mean=findMean(oneList[1])
    oneFeature3Mean=findMean(oneList[2])


    for i in range(len(zeroList)):
        mean.append(findMean(zeroList[i]))

    for i in range(len(oneList)):
        mean1.append(findMean(oneList[i]))

    zMean=findMean(mean)
    oMean=findMean(mean1)

    # print("zero")
    # print(zeroFeature1Mean)
    # print(zeroFeature2Mean)
    # print(zeroFeature3Mean)
    # print(zMean)
    # print("one")
    # print(oneFeature1Mean)
    # print(oneFeature2Mean)
    # print(oneFeature3Mean)
    # print(oMean)
    l1=[zeroFeature1Mean,zeroFeature1Mean,zeroFeature1Mean,zMean]
    l2=[oneFeature1Mean,oneFeature1Mean,oneFeature1Mean,oMean]

    zeroconstant=findMean(l1)
    oneconstant=findMean(l2)
    l1.sort(reverse=True)
    l2.sort(reverse=True)
    coef=findCoef(l1,zeroconstant)
    coef1=findCoef(l2,oneconstant)

    # print("coef",coef,coef1)

    hyper_plane_val=findGroup(l1,coef,zeroconstant,l2,coef1,oneconstant)
    # hyper_plane_val=0.101
    # print(hyper_plane_val)

    return hyper_plane_val

############################################## PREDICTION USING HYPER PLANE##############################

def predictCancer(comb,hyper_plan):
    # print(comb)
    bigListCpy1=[]
    for x in range(len(bigList)):
        smallListCpy1=[]
        for y in range(1,len(bigList[0])):
            if(int(comb[y-1])):
                smallListCpy1.append(bigList[x][y])
        bigListCpy1.append(smallListCpy1)
    zero=0
    one=0
    for i in range(1,len(bigListCpy1)):
        mean=findMean(bigListCpy1[i])
        # print("mean",mean)
        if(hyper_plan > mean):
            bigListCpy1[i].append(0)

        elif(hyper_plan < mean):
            bigListCpy1[i].append(1)
    # print(bigListCpy1)
    count=0
    for x in range(1,len(bigListCpy1)):
            if(bigListCpy1[x][-1]):
                count+=1
    print("No of patients detected with cancer:", end=" ")
    print(count)

    # print("Patients with cancer:")
    # for i in range(len(bigListCpy1)):
    #     if(bigListCpy1[i][-1]):
    #         print(i,bigListCpy1[i])



###################START#####################
smallList=[]
bigList=[]
firstList=[]
secondList=[]
distCost=[]
distanceList1=[]
distanceList2=[]
pointList1=[]
pointList2=[]
classList=[]
bigListCpy=[]
totalCost=[]
sortedCost=[]

###################LOADING TRAINED DATA###############################
workbook = xlrd.open_workbook("cancer_1.xlsx")
worksheet = workbook.sheet_by_index(0)

for i in range(worksheet.nrows):
    smallList=[]
    for j in range(worksheet.ncols):
        smallList.append(worksheet.cell(i, j).value)

    bigList.append(smallList)

for x in range(1,len(bigList)):
    smallListCpy=[]
    for y in range(1,len(bigList[0])-1):
        smallListCpy.append(bigList[x][y])
    bigListCpy.append(smallListCpy)

    if(x<len(bigList)/2):
        firstList.append(smallListCpy)
    else:
        secondList.append(smallListCpy)

##############################BINARY COMBINATION#############################
comb=[]
for i in range(1,(2**len(bigListCpy[1]))):
    comb1=bin(i).split('b')
    comb1=list(comb1[1].zfill(len(firstList[0])))
    totalCost.append(''.join(comb1))


################################SORT FEATURES###################################
ll=totalCost[0]
def getZeroCount(ll):
    count =0
    for x in ll:
        if x == '0':
            count+=1
    return count

getZeroCount(ll)
totalCost.sort(key=lambda x: getZeroCount(x))

##############################FINDING COST#############################
for i in range((2**len(bigListCpy[1]))-1):
    distanceList1.clear()
    distanceList2.clear()
    comb2=list(totalCost[i])
    distanceCal(comb2)


####################SORTING COST AND SELECTING FEATURE###########################
selectiveList =[]
for i,j in zip(totalCost,distCost):
    selectiveList.append([i,j])
selectiveList.sort(key=lambda x:x[1])
selected=selectiveList[0][0]
print("selected combination:")
print(selected)
print()
print("features:")
for x in range(1,len(bigList[0])-1):
    print(bigList[0][x])
print()

print("selected features:")
for x in range (len(selected)):
    if(selected[x] == '1'):
        print(bigList[0][x+1])
print()


################################CLASSIFICATION#################################
hyper_plane=calculateSVM(selected)
workbook1 = xlrd.open_workbook("data (1).xlsx")
worksheet1 = workbook1.sheet_by_index(0)

bigList.clear()
bigListCpy.clear()
firstList.clear()
secondList.clear()
distCost.clear()
distanceList1.clear()
distanceList2.clear()
pointList1.clear()
pointList2.clear()
classList.clear()
for i in range(worksheet1.nrows):
    smallList=[]
    for j in range(worksheet1.ncols):
        smallList.append(worksheet1.cell(i, j).value)
    bigList.append(smallList)

predictCancer(selected,hyper_plane)
######################################## END ######################################
