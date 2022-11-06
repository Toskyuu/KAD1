f = open(r"C:\Users\rober\OneDrive\Pulpit\data.csv")
lines = f.readlines()
f.close()
a = lines[0][0]+lines[0][1]+lines[0][2]
min_dzialki_kielicha = float(a)
max_dzialki_kielicha = float(a)
for x in range(0, len(lines)) :
    b = lines[x][0] + lines[x][1] + lines[x][2]
    b = float(b)
    if(b<min_dzialki_kielicha) : min_dzialki_kielicha = b
    if(b>max_dzialki_kielicha) : max_dzialki_kielicha = b

print("Max_dzialki_kielicha = ", max_dzialki_kielicha, "     Min_dzialki_kielicha = ", min_dzialki_kielicha)


f = open(r"C:\Users\rober\OneDrive\Pulpit\data.csv")
lines = f.readlines()
setosa = 0
versicolor = 0
virginica = 0
for i in range(0, len(lines)):
    if(lines[i][-2] == '0') : setosa = setosa+1
    if(lines[i][-2] == '1') : versicolor = versicolor+1
    if (lines[i][-2] == '2'): virginica = virginica+1

all = setosa+versicolor+virginica
print("Setosa: ", setosa, "(", round(setosa/all*100,1), "%)     Versicolor:: ", versicolor, "(", round(versicolor/all*100,2), "%)   Virginica: ", virginica, "(", round(virginica/all*100,2), "%)" )
f.close()




def wczytaniePlikuDoTablicy(tablicakwiatow) :
    f = open(r"C:\Users\rober\OneDrive\Pulpit\data.csv")
    lines = f.readlines()
    f.close()
    for x in range(0, len(lines)) :
        a = lines[x][0] + lines[x][1] + lines[x][2]
        a = float(a)
        tablicakwiatow[0][x] = a
        a = lines[x][3] + lines[x][4] + lines[x][5]
        a = float(a)
        tablicakwiatow[1][x] = a
        a = lines[x][6] + lines[x][7] + lines[x][8]
        a = float(a)
        tablicakwiatow[2][x] = a
        a = lines[x][9] + lines[x][10] + lines[x][11]
        a = float(a)
        tablicakwiatow[3][x] = a
        a = lines[x][12]
        a = float(a)
        tablicakwiatow[4][x] = a
    print(tablicakwiatow)

tablica = [[],[]]
wczytaniePlikuDoTablicy(tablica)