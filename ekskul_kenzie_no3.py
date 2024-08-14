inputan = input('Masukkan deret bilangan (pisahkan dengan koma): ')
data = []
utkmedian = data.sort()
for bilangan in inputan.split(','):
    data.append(int(bilangan))

#operasimean
x = sum(data)
y = len(data)
z = x/y
#operasimedian
def nilai_tengah(deret):
  deret.sort()
  n = len(deret) # ambil panjang data
  i_tengah = n // 2 # dibulatkan ke bawah

  # jika n adalah ganjil
  if n % 2 == 1:
    return deret[i_tengah]

  # jika n genap
  return (deret[i_tengah - 1] + deret[i_tengah]) / 2

#operasimodus
def nilai_terbanyak(deret):
  # dictionary untuk mapping nilai terbanyak
  peta_kemunculan = {}

  # perulangan satu-persatu tiap bilangan
  for bilangan in deret:
    # periksa apakah sudah pernah muncul atau belum
    if bilangan in peta_kemunculan:
      peta_kemunculan[bilangan] += 1
    else:
      peta_kemunculan[bilangan] = 1

  # cari kemunculan terbanyak
  bilangan_terbesar = deret[0] # ambil angka pertama sebagai yg terbanyak
  for bilangan in peta_kemunculan.keys():
    jumlah = peta_kemunculan[bilangan]

    if jumlah > peta_kemunculan[bilangan_terbesar]:
      bilangan_terbesar = bilangan

  return bilangan_terbesar
while True:
    print("Operasi:")
    print("1. Mean")
    print("2. Median")
    print("3. Modus")
    choice = input("Pilih operasi: ")
 
    if choice == "1":
        print(f"x = {z:.2f}")
    elif choice == "2":
        print(f'Mediannya adalah {nilai_tengah(data)}')
    elif choice == "3":
        print(f'Modusnya adalah {nilai_terbanyak(data)}')
    else:
        print("Pilihan tidak valid")




