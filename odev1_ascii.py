
print("========== ASCII TABLOSU ==========")
print("-----------------------------------")
print("ONDALIK KOD | KARAKTER")
print("-----------------------------------")

for i in range(128):
    if i >= 0 and i <= 31 or i == 127:
        karakter = "Kontrol karakteri"
    elif i == 32 :
        karakter = "[Bosluk]"
    else:
        karakter = chr(i)

    print(f"{i:12} | {karakter}")

print("-----------------------------------")
print("ASCII tablosu tamamlandı.")
