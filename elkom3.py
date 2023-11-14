def banner():
    print("\n \n")

    print("@@@@   @@@@@   @@  @  @   @")
    print("@   @  @   @   @ @ @   @ @")
    print("@   @  @   @   @  @@    @")
    print("@@@@   @@@@@   @   @    @")

    print("\n \n")

def firstFunction(angka):
    return angka ** 3

def secondFunction(angka):
    if angka % 3 == 0:
        return firstFunction(angka)
    else:
        return False

banner()

angka_input = int(input("Masukkan angka: "))

hasil_cek = secondFunction(angka_input)
if hasil_cek is not False:
    print(f"Hasil kubik dari {angka_input} adalah {hasil_cek}.")
else:
    print("False")
