import csv


def min(kwiatki, rodzaj_wielkosci):
    min = float(kwiatki[0][rodzaj_wielkosci])
    for x in kwiatki:
        if float(x[rodzaj_wielkosci]) < min:
            min = float(x[rodzaj_wielkosci])
    return '%.2f' % min


def max(kwiatki, rodzaj_wielkosci):
    max = float(kwiatki[0][rodzaj_wielkosci])
    for x in kwiatki:
        if (float(x[rodzaj_wielkosci]) > max):
            max = float(x[rodzaj_wielkosci])
    return '%.2f' % max

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
        "     Versicolor: ", versicolor, "(", round(versicolor / all * 100, 1), "%)"
        "   Virginica: ", virginica, "(", round(virginica / all * 100, 1), "%)")

    f.close()

def srednia_arytmetyczna(kwiatki, rodzaj_wielkosci):
    suma = 0.0
    for i in range(150):
        suma += float(kwiatki[i][rodzaj_wielkosci])
    return '%.2f' % (suma/150)

def mediana(kwiatki, rodzaj_wielkosci):
    tablica_wielkosci = []
    for x in kwiatki:
        tablica_wielkosci.append(float(x[rodzaj_wielkosci]))

    tablica_wielkosci.sort()

    return '%.2f' % ((tablica_wielkosci[74]+tablica_wielkosci[75])/2)

def kwartylQ1(kwiatki, rodzaj_wielkosci):
    Q1 = []
    # dokladnie 75 elementow
    for x in kwiatki:
        Q1.append(float(x[rodzaj_wielkosci]))
    n = len(kwiatki)
    Q1.sort()
    return '%.2f' % Q1[(n+1)//4]

def kwartylQ3(kwiatki, rodzaj_wialkosci):
    Q3 = []
    for x in kwiatki:
        Q3.append(float(x[rodzaj_wialkosci]))

    Q3.sort()
    n = len(kwiatki)
    return '%.2f' % Q3[((n+1)//4)*3]

def odchylenieStandardowe(kwiatki, rodzaj_wielkosci):
    srednia = float(srednia_arytmetyczna(kwiatki, rodzaj_wielkosci))
    sum = 0
    for x in kwiatki:
        sum += (float(float(x[rodzaj_wielkosci])-srednia)**2)

    sum /= len(kwiatki)
    sum = sum**0.5
    return '%.2f' % sum

f = open(r"data.csv")
csv = csv.reader(f)
kwiatki = []

for row in csv:
    kwiatki.append(row)

f.close()


liczebnosc()
print("\t")

print("Minimum dlugosci dzialki kielicha: " + min(kwiatki, 0))
print("Maksimum dlugosci dzialki kielicha: " + max(kwiatki, 0))
print("Srednia arytmetyczna dlugosci dzialki kielicha: " + srednia_arytmetyczna(kwiatki, 0))
print("Mediana dlugosci dzialki kielicha: " + str(mediana(kwiatki, 0)))
print("Kwartl 1: " + str(kwartylQ1(kwiatki, 0)))
print("Kwartl 3: " + str(kwartylQ3(kwiatki, 0)))
print("Odchylenie standardowe: " + str(odchylenieStandardowe(kwiatki, 0)))
print("\t")

print("Minimum szerokosci dzialki kielicha: " + min(kwiatki, 1))
print("Maksimum szerokosci dzialki kielicha: " + max(kwiatki, 1))
print("Srednia arytmetyczna szerokosci dzialki kielicha: " + srednia_arytmetyczna(kwiatki, 1))
print("Mediana szerokosci dzialki kielicha: " + str(mediana(kwiatki, 1)))
print("Kwartl 1: " + str(kwartylQ1(kwiatki, 1)))
print("Kwartl 3: " + str(kwartylQ3(kwiatki, 1)))
print("Odchylenie standardowe: " + str(odchylenieStandardowe(kwiatki, 1)))
print("\t")

print("Minimum dlugosci platka: " + min(kwiatki, 2))
print("Maksimum dlugosci platka: " + max(kwiatki, 2))
print("Srednia arytmetyczna dlugosci platka: " + srednia_arytmetyczna(kwiatki, 2))
print("Mediana szerokosci dzialki kielicha: " + str(mediana(kwiatki, 2)))
print("Kwartl 1: " +str(kwartylQ1(kwiatki, 2)))
print("Kwartl 3: " +str(kwartylQ3(kwiatki, 2)))
print("Odchylenie standardowe: " + str(odchylenieStandardowe(kwiatki, 2)))
print("\t")

print("Minimum szerokosci platka: " + min(kwiatki, 3))
print("Maksimum szerokosci platka: " + max(kwiatki, 3))
print("Srednia arytmetyczna szerokosci platka: " + srednia_arytmetyczna(kwiatki, 3))
print("Mediana szerokosci dzialki kielicha: " + str(mediana(kwiatki, 3)))
print("Kwartl 1: " +str(kwartylQ1(kwiatki, 3)))
print("Kwartl 3: " +str(kwartylQ3(kwiatki, 3)))
print("Odchylenie standardowe: " + str(odchylenieStandardowe(kwiatki, 3)))
