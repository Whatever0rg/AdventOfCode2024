from collections import Counter
filename = "sampleinput.txt"  

Liste1 = []
Liste2 = []

with open(filename, "r") as file:
    numbers = file.read().split()  
    numbers = list(map(int, numbers))


for i, number in enumerate(numbers):
    if i % 2 == 0:
        Liste1.append(number)
    else:
        Liste2.append(number)

SumListe = []
SpaceListe = []


def SumOfSpaces(Liste1,Liste2): #Task 1
    Liste1.sort()
    Liste2.sort()

    for i in range(len(Liste1)):
        a = Liste1[i]-Liste2[i]
        SpaceListe.append(a)

    for value in SpaceListe:
        if value < 0:
            SumListe.append(-value)
        else:
            SumListe.append(value)

    Sum = sum(SumListe)

    print(Sum)


def SumOfTimes(Liste1,Liste2): # Task 2

    counter = Counter(Liste2)
    CountListe = [counter[element] for element in Liste1]
    

    for i in range(len(Liste1)):
        SumListe.append(Liste1[i]*CountListe[i])

    Sum = sum(SumListe)

    print(Sum)

# Only use one action per run

# SumOfSpaces(Liste1,Liste2)
SumOfTimes(Liste1,Liste2)