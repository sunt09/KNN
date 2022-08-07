import pandas as pd
import numpy as np
# import operator

def EuclideanDistance(data1, data2, dimension):
  dis = 0
  for i in range(dimension):
    dis += np.square(data1[i] - data2[i])
  return np.sqrt(dis)

print(EuclideanDistance([0,0],[1,2],2))

def knn(trainset, testpoint, k):
  dimension = len(testpoint)
  #distance = {index: distance}
  distance = {}
  l = len(trainset)

  #calculate d for each datapoint in trainset
  for i in range(l):
    d = EuclideanDistance(trainset.iloc[i], testpoint, dimension)
    distance[i] = d
  #sort d list
  # sorted_d = sorted(distance.items(), key=operator.itemgetter(1))
  sorted_d = sorted(distance.keys(), key=lambda i:distance[i])
  neighbor = []
  
  #get highest k distance's index
  for i in range(k):
    neighbor.append(sorted_d[i][0])

  classvote = {}
  for i in range(k):
    #response is a specific class selected
    response = trainset.iloc[neighbor[i]][-1]
    classvote[response] = classvote.get(response, 0) + 1

  sorted_c = sorted(classvote.keys(), key= lambda i:classvote[i])
  return sorted_c[0][0]

result = knn(train, testpoint, 3)
print(result)

  
  
  
