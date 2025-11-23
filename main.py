import random

def game_tebak_angka():
    # Komputer memilih angka rahasia antara 1 dan 100
    angka_rahasia = random.randint(1, 100)
    percobaan = 0
    tebakan = 0

    print("Selamat datang di Game Tebak Angka!")
    print("Saya sudah memilih angka antara 1 dan 100. Coba tebak.")

    # Loop utama permainan
    while tebakan != angka_rahasia:
        try:
            # Meminta input dari pengguna
            input_user = input("Masukkan tebakan Anda (1-100): ")
            tebakan = int(input_user)
            percobaan += 1

            if tebakan < angka_rahasia:
                print("Terlalu rendah! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"\nSelamat! Anda menebak angka {angka_rahasia} dengan benar!")
                print(f"Anda membutuhkan {percobaan} percobaan.")
                break # Keluar dari loop

        except ValueError:
            # Menangani jika pengguna memasukkan bukan angka
            print("Input tidak valid. Harap masukkan angka bulat.")

if __name__ == "__main__":
    game_tebak_angka()
