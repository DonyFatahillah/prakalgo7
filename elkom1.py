def banner():
    print("\n \n")

    print("@@@@   @@@@@   @@  @  @   @")
    print("@   @  @   @   @ @ @   @ @")
    print("@   @  @   @   @  @@    @")
    print("@@@@   @@@@@   @   @    @")

    print("\n \n")

def faktorial(n):

    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil

def main():
    banner()
    angka = int(input("Nilai : "))

    hasil = faktorial(angka)

    print(f"faktorial dari {angka} adalah {hasil}")

if __name__ == "__main__":
    main()
