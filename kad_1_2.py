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