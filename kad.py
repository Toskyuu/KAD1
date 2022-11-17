import csv
from matplotlib import pyplot as plt
import math


def findMinimum(table, column):
    min = float(table[0][column])
    for x in kwiatki:
        if float(x[column]) < min:
            min = float(x[column])
    return min


def findMaximum(table, column):
    max = float(table[0][column])
    for x in kwiatki:
        if (float(x[column]) > max):
            max = float(x[column])
    return max


def findQuantity(table, column, searched_value):
    quantity_searched_value = 0
    for x in table:
        if (int(x[column]) == searched_value):
            quantity_searched_value = quantity_searched_value+1
    return quantity_searched_value


def findAverage(table, column):
    sum = 0.0
    for x in table:
        sum += float(x[column])
    return (sum / len(table))


def findMedian(table, column):
    table_to_sort = []
    for x in table:
        table_to_sort.append(float(x[column]))
    table_to_sort.sort()
    middle_value = int(len(table_to_sort)/2)
    if(len(table_to_sort) % 2 == 0):
        return ((table_to_sort[middle_value-1]+table_to_sort[middle_value])/2)
    if(len(table_to_sort) % 2 == 1):
        return middle_value;




def findQ1(table, column):
    Q1 = []
    for x in table:
        Q1.append(float(x[column]))
    n = len(table)
    Q1.sort()
    if (len(Q1) % 4 == 0):
        return Q1[int(len(Q1)/4)]-(Q1[int(len(Q1)/4)]-Q1[int(len(Q1)/4)-1])/4
    if (len(Q1) % 4 == 1):
        return Q1[int(len(Q1)/4)]
    if (len(Q1) % 4 == 2):
        return Q1[int(len(Q1)/4)]+(Q1[int(len(Q1)/4)+1]-Q1[int(len(Q1)/4)])/4
    if (len(Q1) % 4 == 3):
        return (Q1[int(len(Q1)/4)]+Q1[int(len(Q1)/4)+1])/2


def findQ3(table, column):
    Q3 = []
    for x in table:
        Q3.append(float(x[column]))

    Q3.sort()
    if (len(Q3) % 4 == 0):
        return Q3[int(len(Q3) / 4*3)] - (Q3[int(len(Q3) / 4*3)] - Q3[int(len(Q3) / 4*3) - 1]) / 4*3
    if (len(Q3) % 4 == 1):
        return Q3[int(len(Q3) / 4*3)]
    if (len(Q3) % 4 == 2):
        return Q3[int(len(Q3) / 4*3)] - (Q3[int(len(Q3) / 4*3)] - Q3[int(len(Q3) / 4*3)-1]) / 4
    if (len(Q3) % 4 == 3):
        return (Q3[int(len(Q3) / 4*3)] + Q3[int(len(Q3) / 4*3) - 1]) / 2


def findStdDeviation(table, column):
    avg = float(findAverage(table, column))
    sum = 0
    for x in table:
        sum += (float(float(x[column]) - avg) ** 2)

    sum /= len(table)
    sum = sum ** 0.5
    return sum


def rysujHistogram(kwiatki):
    dlugosc_dzialki = []
    szerokosc_dzialki = []
    dlugosc_platka = []
    szerokosc_platka = []
    for x in kwiatki:
        dlugosc_dzialki.append(float(x[0]))
        szerokosc_dzialki.append(float(x[1]))
        dlugosc_platka.append(float(x[2]))
        szerokosc_platka.append(float(x[3]))

    a = round(min(kwiatki, 0), 0)
    b = round(max(kwiatki, 0), 0)
    bins = int(round(math.sqrt(len(dlugosc_dzialki)), 0))
    plt.hist(dlugosc_dzialki, bins=bins, range=(a, b), edgecolor='black')
    plt.title("Długość działki kielicha")
    plt.xlabel("Długość[cm]")
    plt.ylabel("Liczebność")
    plt.show()

    a = round(min(kwiatki, 1), 0)
    b = round(max(kwiatki, 1), 0)
    plt.hist(szerokosc_dzialki, bins=bins, range=(a, b), edgecolor='black')
    plt.title("Szerokość działki kielicha")
    plt.xlabel("Szerokość[cm]")
    plt.ylabel("Liczebność")
    plt.show()

    a = round(min(kwiatki, 2), 0)
    b = round(max(kwiatki, 2), 0)
    plt.hist(dlugosc_platka, bins=bins, range=(a, b), edgecolor='black')
    plt.title("Długość płatka")
    plt.xlabel("Długość[cm]")
    plt.ylabel("Liczebność")
    plt.show()

    a = round(min(kwiatki, 3), 0)
    b = round(max(kwiatki, 3), 0)
    plt.hist(szerokosc_platka, bins=bins, range=(a, b), edgecolor='black')
    plt.title("Szerokość płatka")
    plt.xlabel("Szerokość[cm]")
    plt.ylabel("Liczebność")
    plt.show()

    setosa = []
    versicolor = []
    virginica = []
    nazwy = ["Setosa", "Versicolor", "Virginica"]
    for x in kwiatki:
        if (int(x[4]) == 0):
            setosa.append(float(x[0]))
        elif (int(x[4]) == 1):
            versicolor.append(float(x[0]))
        else:
            virginica.append(float(x[0]))
    razem = [setosa, versicolor, virginica]
    a = round(min(kwiatki, 0), 0)
    b = round(max(kwiatki, 0), 0)
    plt.hist(razem, bins=bins, range=(a, b), edgecolor='black', stacked=True, label=nazwy)
    plt.legend(loc="upper left")
    plt.title("Długość działki kielicha")
    plt.xlabel("Długość[cm]")
    plt.ylabel("Liczebność")
    plt.show()

    setosa = []
    versicolor = []
    virginica = []
    for x in kwiatki:
        if (int(x[4]) == 0):
            setosa.append(float(x[1]))
        elif (int(x[4]) == 1):
            versicolor.append(float(x[1]))
        else:
            virginica.append(float(x[1]))
    razem = [setosa, versicolor, virginica]
    a = round(min(kwiatki, 1), 0)
    b = round(max(kwiatki, 1), 0)
    plt.hist(razem, bins=bins, range=(a, b), edgecolor='black', stacked=True, label=nazwy)
    plt.legend(loc="upper left")
    plt.title("Szerokość działki kielicha")
    plt.xlabel("Szerokość[cm]")
    plt.ylabel("Liczebność")
    plt.show()

    setosa = []
    versicolor = []
    virginica = []
    for x in kwiatki:
        if (int(x[4]) == 0):
            setosa.append(float(x[2]))
        elif (int(x[4]) == 1):
            versicolor.append(float(x[2]))
        else:
            virginica.append(float(x[2]))
    razem = [setosa, versicolor, virginica]
    a = round(min(kwiatki, 2), 0)
    b = round(max(kwiatki, 2), 0)
    plt.hist(razem, bins=bins, range=(a, b), edgecolor='black', stacked=True, label=nazwy)
    plt.legend(loc="upper left")
    plt.title("Długość płatka")
    plt.xlabel("Długość[cm]")
    plt.ylabel("Liczebność")
    plt.show()

    setosa = []
    versicolor = []
    virginica = []
    for x in kwiatki:
        if (int(x[4]) == 0):
            setosa.append(float(x[3]))
        elif (int(x[4]) == 1):
            versicolor.append(float(x[3]))
        else:
            virginica.append(float(x[3]))
    razem = [setosa, versicolor, virginica]
    a = round(min(kwiatki, 3), 0)
    b = round(max(kwiatki, 3), 0)
    plt.hist(razem, bins=bins, range=(a, b), edgecolor='black', stacked=True, label=nazwy)
    plt.legend(loc="upper left")
    plt.title("Szerokość płatka")
    plt.xlabel("Szerokość[cm]")
    plt.ylabel("Liczebność")
    plt.show()


def rysujPudelkowy(kwiatki):
    setosa = []
    versicolor = []
    virginica = []
    nazwy = ["Setosa", "Versicolor", "Virginica"]
    for x in kwiatki:
        if (int(x[4]) == 0):
            setosa.append(float(x[0]))
        elif (int(x[4]) == 1):
            versicolor.append(float(x[0]))
        else:
            virginica.append(float(x[0]))
    razem = [setosa, versicolor, virginica]
    fig, ax = plt.subplots()
    bp = ax.boxplot(razem)
    plt.ylabel("Długość[cm]")
    plt.xlabel("Gatunek")
    plt.xticks([1, 2, 3], nazwy)
    plt.show()

    setosa = []
    versicolor = []
    virginica = []
    for x in kwiatki:
        if (int(x[4]) == 0):
            setosa.append(float(x[1]))
        elif (int(x[4]) == 1):
            versicolor.append(float(x[1]))
        else:
            virginica.append(float(x[1]))
    razem = [setosa, versicolor, virginica]
    fig, ax = plt.subplots()
    bp = ax.boxplot(razem)
    plt.ylabel("Szerokość[cm]")
    plt.xlabel("Gatunek")
    plt.xticks([1, 2, 3], nazwy)
    plt.show()

    setosa = []
    versicolor = []
    virginica = []
    for x in kwiatki:
        if (int(x[4]) == 0):
            setosa.append(float(x[2]))
        elif (int(x[4]) == 1):
            versicolor.append(float(x[2]))
        else:
            virginica.append(float(x[2]))
    razem = [setosa, versicolor, virginica]
    fig, ax = plt.subplots()
    bp = ax.boxplot(razem)
    plt.ylabel("Długość[cm]")
    plt.xlabel("Gatunek")
    plt.xticks([1, 2, 3], nazwy)
    plt.show()

    setosa = []
    versicolor = []
    virginica = []
    for x in kwiatki:
        if (int(x[4]) == 0):
            setosa.append(float(x[3]))
        elif (int(x[4]) == 1):
            versicolor.append(float(x[3]))
        else:
            virginica.append(float(x[3]))
    razem = [setosa, versicolor, virginica]
    fig, ax = plt.subplots()
    bp = ax.boxplot(razem)
    plt.ylabel("Szerokość[cm]")
    plt.xlabel("Gatunek")
    plt.xticks([1, 2, 3], nazwy)
    plt.show()


f = open(r"data.csv")
csv = csv.reader(f)
kwiatki = []

for row in csv:
    kwiatki.append(row)

f.close()

print("Liczebność gatunku setosa = ", findQuantity(kwiatki, 4, 0))
print("Liczebność gatunku versicolor = ", findQuantity(kwiatki, 4, 1))
print("Liczebność gatunku virginica = ", findQuantity(kwiatki, 4, 2))

print("\t")
print("Minimum dlugosci dzialki kielicha: ", '%.2f' %findMinimum(kwiatki, 0))
print("Maksimum dlugosci dzialki kielicha: ", '%.2f' % findMaximum(kwiatki, 0))
print("Srednia arytmetyczna dlugosci dzialki kielicha: ", '%.2f' % findAverage(kwiatki, 0))
print("Mediana dlugosci dzialki kielicha: ", '%.2f' % findMedian(kwiatki, 0))
print("Kwartl 1: ", '%.2f' % findQ1(kwiatki, 0))
print("Kwartl 3: ", '%.2f' % findQ3(kwiatki, 0))
print("Odchylenie standardowe: ", '%.2f' % findStdDeviation(kwiatki, 0))
print("\t")

print("Minimum szerokosci dzialki kielicha: ", '%.2f' % findMinimum(kwiatki, 1))
print("Maksimum szerokosci dzialki kielicha: ", '%.2f' % findMaximum(kwiatki, 1))
print("Srednia arytmetyczna szerokosci dzialki kielicha: ", '%.2f' % findAverage(kwiatki, 1))
print("Mediana szerokosci dzialki kielicha: ", '%.2f' % findMedian(kwiatki, 1))
print("Kwartl 1: ", '%.2f' % findQ1(kwiatki, 1))
print("Kwartl 3: ", '%.2f' % findQ3(kwiatki, 1))
print("Odchylenie standardowe: ", '%.2f' % findStdDeviation(kwiatki, 1))
print("\t")

print("Minimum dlugosci platka: ", '%.2f' % findMinimum(kwiatki, 2))
print("Maksimum dlugosci platka: ", '%.2f' % findMaximum(kwiatki, 2))
print("Srednia arytmetyczna dlugosci platka: ", '%.2f' % findAverage(kwiatki, 2))
print("Mediana dlugosci platka: ", '%.2f' % findMedian(kwiatki, 2))
print("Kwartyl 1: ", '%.2f' % findQ1(kwiatki, 2))
print("Kwartyl 3: ", '%.2f' % findQ3(kwiatki, 2))
print("Odchylenie standardowe: ", '%.2f' % findStdDeviation(kwiatki, 2))
print("\t")

print("Minimum szerokosci platka: ", '%.2f' % findMinimum(kwiatki, 3))
print("Maksimum szerokosci platka: ", '%.2f' % findMaximum(kwiatki, 3))
print("Srednia arytmetyczna szerokosci platka: ", '%.2f' % findAverage(kwiatki, 3))
print("Mediana szerokosci dzialki kielicha: ", '%.2f' % findMedian(kwiatki, 3))
print("Kwartyl 1: ", '%.2f' % findQ1(kwiatki, 3))
print("Kwartyl 3: ", '%.2f' % findQ3(kwiatki, 3))
print("Odchylenie standardowe: ", '%.2f' % findStdDeviation(kwiatki, 3))

# rysujHistogram(kwiatki)
# rysujPudelkowy(kwiatki)
