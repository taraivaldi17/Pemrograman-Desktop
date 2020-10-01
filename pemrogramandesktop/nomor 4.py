x = []
angka = int(input("limit nilai: "))

for i in range(angka):
    inp = float(input("masukkan nilai: "))
    x.append(inp)

print('\nnilai maximum =', max(x))
print('nilai minimum =', min(x))
