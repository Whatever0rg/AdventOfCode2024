from collections import Counter
filename = "input.txt"  

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
print(Liste1,';',Liste2)

def SumOfSpaces(Liste1,Liste2):
    Liste1.sort()
    Liste2.sort()
    print(Liste1,';',Liste2)


    for i in range(len(Liste1)):
        a = Liste1[i]-Liste2[i]
        SpaceListe.append(a)


    print(SpaceListe)
    for value in SpaceListe:
        if value < 0:
            SumListe.append(-value)
        else:
            SumListe.append(value)

    print(SumListe)
    Sum = sum(SumListe)

    print(Sum)


def SumOfTimes(Liste1,Liste2):

    counter = Counter(Liste2)
    CountListe = [counter[element] for element in Liste1]
    print(CountListe)

    for i in range(len(Liste1)):
        SumListe.append(Liste1[i]*CountListe[i])
    print(SumListe)
    Sum = sum(SumListe)

    print(Sum)

SumOfTimes(Liste1,Liste2)