
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