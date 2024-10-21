# Kalkulator Sederhana
print("Kalkulator Sederhana")

angka_1 = float(input("masukkan angka 1 = "))
opertator = input("operator (+,-,*,/) : ")
angka_2 = float(input("masukkan angka 2 = "))

# Percabangannya
if opertator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil}")
elif opertator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif opertator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif opertator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
print("Sekian Terima Kasih")