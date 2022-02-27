from ast import match_case
from sklearn import datasets
from showConvexHull import showConvexHull
import pandas as pd

print("Pilih dataset:")
print("1. iris")
print("2. breast cancer")
print("3. wine")
command = input(">> ")
print()
def data_set(x):
    match x:
        case 1:
            return datasets.load_iris()
        case 2:
            return datasets.load_breast_cancer()
        case 3:       
            return datasets.load_wine()
        case _:
            return None

data = data_set(int(command))

# create a DataFrame

for i in range(len(data.feature_names)): 
    print(f"{i+1}. ", end="")
    print(data.feature_names[i])

print()

x = int(input("Pilih nomor kolom untuk menjadi variabel x: "))
y = int(input("Pilih nomor kolom untuk menjadi variabel y: "))

showConvexHull(data, x - 1 , y - 1)

