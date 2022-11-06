import csv


def min(kwiatki, rodzaj_wielkosci):
    min = float(kwiatki[0][rodzaj_wielkosci])
    for x in kwiatki:
        if (float(x[rodzaj_wielkosci]) < min):
            min = float(x[rodzaj_wielkosci])
    return '%.2f' % min


def max(kwiatki, rodzaj_wielkosci):
    max = float(kwiatki[0][rodzaj_wielkosci])
    for x in kwiatki:
        if (float(x[rodzaj_wielkosci]) > max):
            max = float(x[rodzaj_wielkosci])
    return '%.2f' % max


f = open(r"data.csv")
csv = csv.reader(f)
kwiatki = []
for row in csv:
    kwiatki.append(row)

print(min(kwiatki, 0))
print(max(kwiatki,0))
f.close()
