unlilar = "aeiouAEIOU"

matn = input("Matn kiriting: ")

soni = 0
for harf in matn:
    if harf in unlilar:
        soni += 1

print(f"Matnda {soni} ta unli harf bor.")
