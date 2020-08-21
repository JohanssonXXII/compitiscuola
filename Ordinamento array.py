import random

random.seed()   #Prepare random number generator

numeri = [0] * (1000)

for i in range(0, 999 + 1, 1):
    numeri[i] = int(random.random() * 1000)
for i in range(0, 999 + 1, 1):
    print(numeri[i])
for i in range(1, 999 + 1, 1):
    temp = numeri[i]
    j = i - 1
    while numeri[j] > temp and j >= 0:
        numeri[j + 1] = numeri[j]
        j = j - 1
    numeri[j + 1] = temp
print("Array dopo l'ordinamento")
for i in range(0, 999 + 1, 1):
    print(numeri[i])
