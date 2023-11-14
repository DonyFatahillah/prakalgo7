def banner():
    print("\n \n")

    print("@@@@   @@@@@   @@  @  @   @")
    print("@   @  @   @   @ @ @   @ @")
    print("@   @  @   @   @  @@    @")
    print("@@@@   @@@@@   @   @    @")

    print("\n \n")

def hitung(word): #inputKata
    jumlahVokal = 0
    jumlahKonsonan = 0

    vokal = "aiueo"

    word = word.lower()

    for i in word:
        if i.isalpha():
            if i in vokal:
                jumlahVokal += 1
            else:
                jumlahKonsonan += 1
    
    return jumlahVokal, jumlahKonsonan

banner()

inputKata = input("masukan kata : ")

vokal, konsonan = hitung(inputKata)

print(f"Jumlah Vokal = {vokal}")
print(f"Jumlah Konsonan = {konsonan}")
