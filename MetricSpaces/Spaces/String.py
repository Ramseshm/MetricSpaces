# -*- coding: utf-8 -*-
"""String.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HDO9YXM7qdbqG5AbhFrNXLwwoZdt-qa4
"""

dix=[""]
#db=open("/content/drive/MyDrive/test.txt").read().split()

def loadDB(dbloc):
  db=open(dbloc).read().split()
  aux=list()
  for i in db:
    aux.append(i)
  global dix
  dix.extend(aux)
  return len(db)

def cleandix():
  global dix
  dix=[""]

def Distance(i,j):
  return dist(dix[i],dix[j])

def add(str1):
  dix[0]=str1

def pop():
  dix[0]=" "

def tam():
  return len(dix)

def printObj(i,d):
  print(f'{dix[i]}---> {d}')

def name():
  return "String"

def dist(str1,str2):
  d=dict()
  for i in range(len(str1)+1):
     d[i]=dict()
     d[i][0]=i
  for i in range(len(str2)+1):
     d[0][i] = i
  for i in range(1, len(str1)+1):
     for j in range(1, len(str2)+1):
        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not str1[i-1] == str2[j-1]))
  return d[len(str1)][len(str2)]