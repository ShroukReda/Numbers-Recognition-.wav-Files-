import csv
import pandas as pd
import nltk
from nltk.stem import*
list =[]
Answers =[]
Quections =[]
StemmingQuections =[]
StemmingAnswers =[]
counter = 0
def ReadAllData(Path):
    with open('/home/mohammed/Downloads/Train.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            list.append(row)
    csvFile.close()
    return list
def ConstructData(List):
    for i in range(1,len(List)):
        Answers.append(List[i][1])
        Quections.append(List[i][2])
    return Quections , Answers
def ApplyStemmingAndToknization(data , var):
    stemmer = PorterStemmer()
    for index in range(0 , len(data)):
        Words = data[index].split()
        StemmingWords = [stemmer.stem(plural) for plural in Words]
        encoded_string = [s.encode('UTF-8', 'strict') for s in StemmingWords]
        Out_Temp = ' '.join(encoded_string)
        var.append(Out_Temp)
    return var
def DataPreprocessing(Path , StemmingQuections ,StemmingAnswers ):
    a = ReadAllData(Path)
    b, c = ConstructData(a)
    StemmingQuections = ApplyStemmingAndToknization(b, StemmingQuections)
    StemmingAnswers = ApplyStemmingAndToknization(c, StemmingAnswers)
    return StemmingQuections ,StemmingAnswers

A , B =DataPreprocessing("hapd",StemmingQuections , StemmingAnswers)
print (A)
print (B)