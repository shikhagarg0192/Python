# -*- coding: cp1252 -*-
from numpy import *
import numpy
import operator
from os import listdir
#create a dataset for testing the classifier classify0()
def createdataset() :
        group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
        labels = ['A','A','B','B']
        return group, labels


def classify0(inX, dataSet, labels, k) :
        #get the size of group : 4 in this case
        dataSetSize = dataSet.shape[0]
        #create an array with inX data datsetsize times - dataset (xi - x(i-1))
        diffMat = tile(inX,(dataSetSize,1))-dataSet
        #calculate there square
        sqDiffMat = diffMat**2
        #sqd = (xi-x(i-1)) + (yi - y(i-1))
        sqDistances = sqDiffMat.sum(axis=1)
        #d= sqrt(sqd)
        distances = sqDistances**0.5
        # sort the nodes according to their distance from input data in increasing order
        sortedDistIndicies = distances.argsort()
        # create a dictionery ; initially null
        classCount={}
        # k is the no. of nodes we'll take in account to predict the label for input data
        for i in range(k):
                #label of ith node; so, if 1st node, it will be A in our case
                voteIlabel = labels[sortedDistIndicies[i]]
                #as dictionery is null initially, so it wont get anything from there hence 0. 0+ 1 = 1. so our dictionery becomes {'A': 2} and finally in last k=3 run, {'A': 2, 'B': 1}
                classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        #sort the classcount dictionery in reverse and get the nearest label on top
        sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1), reverse=True)
        #return the label on top :)
        return sortedClassCount[0][0]

def file2matrixonly(filename):
        #open the file filename
        fr = open(filename)
        #no. of lines in file
        numberOfLines = len(fr.readlines())
        #create a matrix n * 7 full of zeroes
        returnMat = zeros((numberOfLines,7))
        fr = open(filename)
        index = 0
        for line in fr.readlines():
                #remove the return line character from each line
                line = line.strip()
                #split the line delimited by a ,
                listFromLine = line.split(',')
                #in the whole row of returnmat which was filled with 0s, store the rows from the file.
                returnMat[index,:] = listFromLine[0:7]
                #put labels' numerical values in classlabelvector
                index += 1
        return returnMat

def file2matrix(filename):
        #open the file filename
        fr = open(filename)
        #no. of lines in file
        numberOfLines = len(fr.readlines())
        #create a matrix n * 3 full of zeroes
        returnMat = zeros((numberOfLines,7))
        classLabelVector = []
        fr = open(filename)
        index = 0
        for line in fr.readlines():
                #remove the return line character from each line
                line = line.strip()
                #split the line delimited by a tab
                listFromLine = line.split(',')
                #in the whole row of returnmat which was filled with 0s, store the rows from the file.
                returnMat[index,:] = listFromLine[0:7]
                #put labels' numerical values in classlabelvector
                classLabelVector.append(int(listFromLine[-1]))
                index += 1
        return returnMat,classLabelVector
#returns labels and matrix separately


def file2matrix2(filename):
        #open the file filename
        fr = open(filename)
        #no. of lines in file
        numberOfLines = len(fr.readlines())
        #create a matrix n * 3 full of zeroes
        returnMat = zeros((numberOfLines,3))
        classLabelVector = []
        fr = open(filename)
        index = 0
        for line in fr.readlines():
                #remove the return line character from each line
                line = line.strip()
                #split the line delimited by a tab
                listFromLine = line.split('\t')
                #in the whole row of returnmat which was filled with 0s, store the rows from the file.
                returnMat[index,:] = listFromLine[0:3]
                #put labels' numerical values in classlabelvector
                classLabelVector.append(int(listFromLine[-1]))
                index += 1
        return returnMat,classLabelVector
#returns labels and matrix separately


#for normalizing the data. bringing all the values down between 0 and 1 so that computation becomes easier and moreover, to keep the values same.
def autonorm(dataset):
        #min values of each feature
        minvals = dataset.min(0)
        #max val
        maxvals = dataset.max(0)
        #range of the difference
        ranges = maxvals-minvals
        #creating a matrix of same size as dataset but filled with 0s
        normdataset = zeros(shape(dataset))
        #size of dataset
        m= dataset.shape[0]
        #tile(a,(b,c)) duplicates a b times and increase the dimension by c. so, this is old value - min
        normdataset = dataset - tile(minvals, (m,1))
        # old value - min / max - min
        normdataset = normdataset / tile(ranges, (m,1))
        # returns normalized dataset, range and min values
        return normdataset, ranges, minvals


def datingClassTest():
        #division between test dataset and training dataset
        hoRatio = 0.10
        #file to matrix conversion
        datingDataMat,datingLabels = file2matrix('datatestset.txt')
        #normalizing the data values in data set
        normMat, ranges, minVals = autonorm(datingDataMat)
        m = normMat.shape[0]
        #no. of rows in test set
        numTestVecs = int(m*hoRatio)
        #error count starting
        errorCount = 0.0
        for i in range(numTestVecs):
                #returns the appropriate label for the first row
                classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],\
                        datingLabels[numTestVecs:m],5)
                print "the classifier came back with: %d, the real answer is: %d"\
                        % (classifierResult, datingLabels[i])
                if (classifierResult != datingLabels[i]): errorCount += 1.0
        print "the total error rate is: %f" % (errorCount/float(numTestVecs))



def classifyPerson():
        resultList = ['not at all','in small doses', 'in large doses']
        #takes input from user
        percentTats = float(raw_input(\
                "percentage of time spent playing video games?"))
        ffMiles = float(raw_input("frequent flier miles earned per year?"))
        iceCream = float(raw_input("liters of ice cream consumed per year?"))
        datingDataMat,datingLabels = file2matrix('datatestSet.txt')
        normMat, ranges, minVals = autonorm(datingDataMat)
        inArr = array([ffMiles, percentTats, iceCream])
        #inX = input - min vals / ranges, dataset = normdata, labels = dating labels, k =3
        classifierResult = classify0((inArr-\
                minVals)/ranges,normMat,datingLabels,3)
        print "You will probably like this person: ",\
                resultList[classifierResult - 1]


#for handwriting alphabets classification
def img2vector(filename):
        #creates a vector of 1024 columns
        returnVect = zeros((1,1024))
        fr = open(filename)
        for i in range(32):
                lineStr = fr.readline()
                for j in range(32):
                        returnVect[0,32*i+j] = int(lineStr[j])
        return returnVect
#so basically we have few files of each no. like 0 , 1 ,2... 9.
#and each file has 1024 binary digits in it in form of 32*32 matrix.
#this function puts those 1024 digits in a row.
#so, it appends the next row at the end if the previous one.

def handwritingClassTest():
        hwLabels = [] #will contain the labels fetched by splitting the name of the file.
        trainingFileList = listdir('digits/trainingDigits')
        m = len(trainingFileList)
        trainingMat = zeros((m,1024))
        for i in range(m):
                fileNameStr = trainingFileList[i]
                fileStr = fileNameStr.split('.')[0]
                classNumStr = int(fileStr.split('_')[0])
                hwLabels.append(classNumStr)
                trainingMat[i,:] = img2vector('digits/trainingDigits/%s' % fileNameStr)
        testFileList = listdir('digits/testDigits')
        errorCount = 0.0
        mTest = len(testFileList)
        for i in range(mTest):
                fileNameStr = testFileList[i]
                fileStr = fileNameStr.split('.')[0]
                classNumStr = int(fileStr.split('_')[0])
                vectorUnderTest = img2vector('digits/testDigits/%s' % fileNameStr)
                classifierResult = classify0(vectorUnderTest, \
                        trainingMat, hwLabels, 3)
                print "the classifier came back with: %d, the real answer is: %d"\
                        % (classifierResult, classNumStr)
                if (classifierResult != classNumStr): errorCount += 1.0
        print "\nthe total number of errors is: %d" % errorCount
        print "\nthe total error rate is: %f" % (errorCount/float(mTest))

def titanicClassTest():
        DataMat,Labels = file2matrix('train.csv')
        #normalizing the data values in data set
        normMat, ranges, minVals = autonorm(DataMat)
        testmat = file2matrixonly('test.csv')
        m = testmat.shape[0]

        #error count starting
        errorCount = 0.0
        
        for i in range(m):
                #returns the appropriate label for the first row
                classifierResult = classify0(testmat[i,:],normMat,Labels,5)
                print " %d" % classifierResult
        
