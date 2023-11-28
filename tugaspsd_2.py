def nabungatas(nominal, lt):
    lt.insert(0, nominal)

def nabungbawah(nominal, lt):
    lt.append(nominal)

def ambilatas(lt):
    lt.pop(0)

def ambilbawah(lt):
    lt.pop(-1)


def main():
    step = int(input("inputkan berapa kali langkahnya = "))

    langkah = []

    while step > 0:
        temp = input("masukkan perintah <spasi> nominal = ").split(" ")
        langkah.append(temp)
        step -= 1

    #pemisahan
    tabungan = []

    for i in langkah:
        i = list(map(int, i))
        if i[0] == 0:
            nabungatas(i[1], tabungan)
        elif i[0] == 1:
            nabungbawah(i[1], tabungan)
        elif i[0] == 2:
            if len(tabungan) < 1:
                print("tabungan anda sudah kosong gak bisa diambil dari atas")
                break
            ambilatas(tabungan)
        elif i[0] == 3:
            if len(tabungan) < 1:
                print("tabungan anda sudah kosong gak bisa diambil dari bawah")
                break
            ambilbawah(tabungan)

    if len(tabungan) > 0:
        print(sum(tabungan))
    else:
        print("tabungan anda kosong!")

main()