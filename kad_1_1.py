import csv
from matplotlib import pyplot as plt
import math


def min(kwiatki, rodzaj_wielkosci):
    min = float(kwiatki[0][rodzaj_wielkosci])
    for x in kwiatki:
        if float(x[rodzaj_wielkosci]) < min:
            min = float(x[rodzaj_wielkosci])
    return min


def max(kwiatki, rodzaj_wielkosci):
    max = float(kwiatki[0][rodzaj_wielkosci])
    for x in kwiatki:
        if (float(x[rodzaj_wielkosci]) > max):
            max = float(x[rodzaj_wielkosci])
    return max


def liczebnosc():
    f = open(r"data.csv")
    lines = f.readlines()
    setosa = 0
    versicolor = 0
    virginica = 0
    for i in range(0, len(lines)):
        if (lines[i][-2] == '0'): setosa = setosa + 1
        if (lines[i][-2] == '1'): versicolor = versicolor + 1
        if (lines[i][-2] == '2'): virginica = virginica + 1
    all = setosa + versicolor + virginica
    print("Setosa: ", setosa, "(", round(setosa / all * 100, 1), "%)"
                                                                 "     Versicolor: ", versicolor, "(",
          round(versicolor / all * 100, 1), "%)"
                                            "   Virginica: ", virginica, "(", round(virginica / all * 100, 1), "%)")

    f.close()


def srednia_arytmetyczna(kwiatki, rodzaj_wielkosci):
    suma = 0.0
    for i in range(150):
        suma += float(kwiatki[i][rodzaj_wielkosci])
    return (suma / 150)


def mediana(kwiatki, rodzaj_wielkosci):
    tablica_wielkosci = []
    for x in kwiatki:
        tablica_wielkosci.append(float(x[rodzaj_wielkosci]))

    tablica_wielkosci.sort()

    return ((tablica_wielkosci[74] + tablica_wielkosci[75]) / 2)


def kwartylQ1(kwiatki, rodzaj_wielkosci):
    Q1 = []
    # dokladnie 75 elementow
    for x in kwiatki:
        Q1.append(float(x[rodzaj_wielkosci]))
    n = len(kwiatki)
    Q1.sort()
    return Q1[(n + 1) // 4]


def kwartylQ3(kwiatki, rodzaj_wialkosci):
    Q3 = []
    for x in kwiatki:
        Q3.append(float(x[rodzaj_wialkosci]))

    Q3.sort()
    n = len(kwiatki)
    return Q3[((n + 1) // 4) * 3]


def odchylenieStandardowe(kwiatki, rodzaj_wielkosci):
    srednia = float(srednia_arytmetyczna(kwiatki, rodzaj_wielkosci))
    sum = 0
    for x in kwiatki:
        sum += (float(float(x[rodzaj_wielkosci]) - srednia) ** 2)

    sum /= len(kwiatki)
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
    plt.hist(dlugosc_dzialki, bins=bins, range=(a,b), edgecolor='black')
    plt.title("Długość działki kielicha")
    plt.xlabel("Długość[cm]")
    plt.ylabel("Liczebność")
    plt.show()

    a = round(min(kwiatki,1), 0)
    b = round(max(kwiatki,1), 0)
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
        if(int(x[4]) == 0):
            setosa.append(float(x[0]))
        elif(int(x[4]) == 1):
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
        if(int(x[4]) == 0):
            setosa.append(float(x[1]))
        elif(int(x[4]) == 1):
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
    plt.xticks([1,2,3], nazwy)
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

liczebnosc()
print("\t")

print("Minimum dlugosci dzialki kielicha: ", '%.2f' % min(kwiatki, 0))
print("Maksimum dlugosci dzialki kielicha: ", '%.2f' % max(kwiatki, 0))
print("Srednia arytmetyczna dlugosci dzialki kielicha: ", '%.2f' % srednia_arytmetyczna(kwiatki, 0))
print("Mediana dlugosci dzialki kielicha: ", '%.2f' % mediana(kwiatki, 0))
print("Kwartl 1: ", '%.2f' % kwartylQ1(kwiatki, 0))
print("Kwartl 3: ", '%.2f' % kwartylQ3(kwiatki, 0))
print("Odchylenie standardowe: ", '%.2f' % odchylenieStandardowe(kwiatki, 0))
print("\t")

print("Minimum szerokosci dzialki kielicha: ", '%.2f' % min(kwiatki, 1))
print("Maksimum szerokosci dzialki kielicha: ", '%.2f' % max(kwiatki, 1))
print("Srednia arytmetyczna szerokosci dzialki kielicha: ", '%.2f' % srednia_arytmetyczna(kwiatki, 1))
print("Mediana szerokosci dzialki kielicha: ", '%.2f' % mediana(kwiatki, 1))
print("Kwartl 1: ", '%.2f' % kwartylQ1(kwiatki, 1))
print("Kwartl 3: ", '%.2f' % kwartylQ3(kwiatki, 1))
print("Odchylenie standardowe: ", '%.2f' % odchylenieStandardowe(kwiatki, 1))
print("\t")

print("Minimum dlugosci platka: ", '%.2f' % min(kwiatki, 2))
print("Maksimum dlugosci platka: ", '%.2f' % max(kwiatki, 2))
print("Srednia arytmetyczna dlugosci platka: ", '%.2f' % srednia_arytmetyczna(kwiatki, 2))
print("Mediana szerokosci dzialki kielicha: ", '%.2f' % mediana(kwiatki, 2))
print("Kwartl 1: ", '%.2f' % kwartylQ1(kwiatki, 2))
print("Kwartl 3: ", '%.2f' % kwartylQ3(kwiatki, 2))
print("Odchylenie standardowe: ", '%.2f' % odchylenieStandardowe(kwiatki, 2))
print("\t")

print("Minimum szerokosci platka: ", '%.2f' % min(kwiatki, 3))
print("Maksimum szerokosci platka: ", '%.2f' % max(kwiatki, 3))
print("Srednia arytmetyczna szerokosci platka: ", '%.2f' % srednia_arytmetyczna(kwiatki, 3))
print("Mediana szerokosci dzialki kielicha: ", '%.2f' % mediana(kwiatki, 3))
print("Kwartl 1: ", '%.2f' % kwartylQ1(kwiatki, 3))
print("Kwartl 3: ", '%.2f' % kwartylQ3(kwiatki, 3))
print("Odchylenie standardowe: ", '%.2f' % odchylenieStandardowe(kwiatki, 3))

# rysujHistogram(kwiatki)
# rysujPudelkowy(kwiatki)
