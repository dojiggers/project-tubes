def hitung_kapital(kalimat, indexMulai, total = 0):
    try:
        if indexMulai > len(kalimat):
            raise AssertionError()
    except AssertionError:
        print("indexMulai akan diubah menjadi 0")
        indexMulai = 0
    finally:
        if indexMulai == len(kalimat):
            return total
        if kalimat[indexMulai].isupper():
            total += 1
        return hitung_kapital(kalimat, indexMulai+1,total)

kalimat = input("Kalimat : ")
print(hitung_kapital(kalimat,0))