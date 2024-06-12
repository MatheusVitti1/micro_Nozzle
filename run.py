#Retirando valores de R e T para calcular o MPS
import os
import re
import numpy as np
import math

os.system('touch simulation.foam')

f = open("constant/DVMProperties", "r")
lines = f.readlines()
R_line = lines[26]

R_numbers = re.findall('\d+\.\d+|\d+',R_line)
R = float(R_numbers[7])

T_line = lines[28]
T_number = re.findall('\d+\.\d+|\d+',T_line)
T = float(T_number[7])

print("T = {}".format(T))
print("R = {}".format(R))

#Calculando MPS:

def MPS(T,R):
	return(math.sqrt(2*R*T))
print("MPS = {}".format(MPS(T,R)))

#Escrevendo Xis e Weights:
n = 28
os.system('python ~/OpenFOAM/vitti-6/applications/dugksFoam/src/scripts/setDV.py GH {} {}'.format(MPS(T,R),n))

#Criando a malha:

os.system('blockMesh')
