"""
Gimana cara filter data ya?

Haikal ingin mencoba filter isi data array yang diberikan oleh temannya, yaitu array yang berisi angka-angka
tantangan yang diberikan oleh temannya adalah hanya berisi nilai ganjil.
bantu Haikal untuk menyelesaikan tantangan tersebut.

Contoh
Input:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

Output:
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
"""
arr = range(1, 20)
# lanjutkan code dibawah ini

hasil = [angka for angka in arr if angka % 2 != 0]
print(hasil)

#ini pake chatgpt