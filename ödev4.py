n = int(input("n sayısını giriniz: "))

toplam = 0
cift_toplam = 0
bes_toplam = 0
faktoriyel = 1

a = 0
b = 1

print("Fibonacci serisi:")

for i in range(1, n + 1):

    toplam = toplam + i

    if i % 2 == 0:
        cift_toplam = cift_toplam + i

    if i % 5 == 0:
        bes_toplam = bes_toplam + i

    faktoriyel = faktoriyel * i

    print(a, end=" ")
    a, b = b, a + b

print("\nTüm sayıların toplamı:", toplam)
print("Çift sayıların toplamı:", cift_toplam)
print("5'in katlarının toplamı:", bes_toplam)
print(n, "sayısının faktöriyeli:", faktoriyel)

if a != 0:
    altin_oran = b / a
    print("Altın oran:", altin_oran)