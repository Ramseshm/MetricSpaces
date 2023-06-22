import math
from scipy.spatial import distance
import numpy as np
dix=[[]]
def loadDB(dbloc):
  db=open(dbloc).readlines()
  aux=list()
  for i in db:
    aux.append(list((i.split())))
  for j in range(len(aux)):
    aux[j]=[float(x) for x in aux[j]]
  global dix
  dix.extend(aux)
  return len(db)

def add(v):
  dix[0]=list(v)
def pop():
  dix[0]=[]
def tam():
  return len(dix)

def printObj(x,r):
  print(f"{x}---->{r}")

def name():
  return "vectors"
  
def cleandix():
  global dix
  dix=[[]]

def Distance(i,j):
  distan=distance.euclidean(dix[i],dix[j])
  #distan = np.linalg.norm(np.array(dix[i])-np.array(dix[j]))
  return distan