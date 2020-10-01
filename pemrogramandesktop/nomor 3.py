Berat = float(input("Masukkan Berat Badan (kg) : "))
Tinggi = float(input("Masukkan Tinggi Badan (m) : "))

BMI = Berat/(Tinggi*Tinggi)
print("BMI = ",'{:.2f}'.format(BMI))
 
if BMI > 30:
    print ("Obesitas")
elif BMI >23:
    print ("Kecenderungan obesitas")
elif BMI >18.5:
    print ("Berat Badan normal")
else:
    print ("Berat Badan kurang")

