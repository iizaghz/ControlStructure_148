a = float (input("Masukkan angka pertama: "))
b = float (input("Masukkan angka kedua: "))
c = float (input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
elif c >= a and c >= b:
    largest = b
else:
    print("Tidak ada nilai terbesar")

print("Angka terbesar adalah", largest)


