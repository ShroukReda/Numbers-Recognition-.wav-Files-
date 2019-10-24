import cv2
import pandas as pd
import numpy as np
import scipy.misc
import os
import sklearn
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
from sklearn import svm
from random import shuffle
import tensorflow as tf
import matplotlib.image as mpimg
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from PIL import Image, ImageDraw, ImageFont
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import librosa

def MinLen(L):
    m=90
    for i in L:
        x=len(i)
        if x<m:
            m=x
    return m
def Avg(L):
    ML=[]
    for i in L:
        i=i.mean(axis=1)
        ML.append(i)
    return ML
def Trim(L):
    NL=[]
    for i in L:
        x=i.shape
        r=x[1]
        if r>15:
            d=r-15
            i=np.delete(i, np.s_[-d:], axis=1)
            #i=i[:][:-d]
            NL.append(i)
        else:
            NL.append(i)
    return NL

TRAIN_DIR = 'train'
TEST_DIR = 'test'
f=[]
labels=[]
for a in (os.listdir(TRAIN_DIR)):
    audio_path = os.path.join(TRAIN_DIR, a)
    x , sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(x, sr=sr)
    mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
    f.append(mfcc)
    labels.append(int(a[0]))
TF=[]
Tlabels=[]
for a in (os.listdir(TEST_DIR)):
    audio_path = os.path.join(TEST_DIR, a)
    x , sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(x, sr=sr)
    mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
    TF.append(mfcc)
    Tlabels.append(int(a[0]))

f=Trim(f)
m=Avg(f)


TF=Trim(TF)
tm=Avg(TF)

X_tarin= np.array(m)
y_train= labels

X_test= np.array(tm)
y_test= Tlabels

clf = svm.SVC(gamma=0.001, C=10)
clf.fit(X_tarin, y_train)
acc=0
prediction=clf.predict(X_test)
for i in range(len(prediction)):
    if prediction[i]==Tlabels[i]:
        acc+=1
print((acc/len(prediction)*100),'%')
