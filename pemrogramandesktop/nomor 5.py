user = "Admin"
pas = "root"

for i in range(3):
    username = input("Masukkan User     :")
    password = input("Masukkan Password :")

    if username == user and password == pas:
        print ("\nAnda berhasil masuk")
        break
    else:
        print ("\nAnda gagal masuk\n")
