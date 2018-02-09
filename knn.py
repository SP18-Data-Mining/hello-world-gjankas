import csv
import math
import sys

terms = []
dataObjectCount = 0 
testData = []
trainingData = []

with open('fruit_data_with_colors.txt','r') as tsv:
#	print(dataObjectCount)
	for line in tsv :
		if dataObjectCount % 5 == 0 :
			testData.append(line.strip().split('\t'))
	else :
		trainingData.append(line.strip().split('\t'))
	dataObjectCount = dataObjectCount + 1
		
print("Test Data" + str(testData))
print('\n\n\n\n\n\n\n')
print("Training data" + str(trainingData))

trainingFeatures = []
testFeatures = []
trainingLabels = []
incremet = 0
for line in trainingData :
	incremet += 1
	dataObject = []
	if incremet == 5 or incremet == 6:
			dataObject.append(float(line))
for line in testData:
    dataObject=[]
if incremet == 5 or incremet == 6:
	dataObject.append(float(line))
testFeatures.append(dataObject)

import math 
def euclideanDistance(instnace1, instance2, length):
	distance = 0 
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

# calculations 
import operator
def getNeighbors(trainingSet, testInstance, k):
	distnace = []
	length = len(testInstance) - 1
	for x in range (len(trainingSet)) :
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distance.append((trainingSet[x], dist))
	distnace.sort(key=opperator.itemgetter(1))
	neighbors = []
	for x in range (k) :
		neighbors.append(distance[x][0])
	return neighbors 

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] is predictions[x]:
			correct += 1
		return (correct/float(len(testSet))) * 100.0
# prints out training data, distance, and label
	print("Trainnig Data = ",neighbor)
	print("Distance = ", incremet)
	print("Label = ", trainingLabels[neighbor])
