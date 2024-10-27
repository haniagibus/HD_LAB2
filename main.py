from faker import Faker
import csv
import random
fake = Faker()

dane_wizyty=[]
#Pacjenci
for i in range(1000):
    ID_pacjenta=random.randint(1000000900,999999999)
    dane_wizyty.append(ID_pacjenta, fake.name())

for i in range(1000):
    print(f"{i}: {dane_wizyty[i]}")


# # Zapis do pliku CSV
# with open("dane.csv", mode="w", newline="") as plik_csv:
#     nazwy_pol = ["id", "nazwa", "cena"]
#     writer = csv.DictWriter(plik_csv, fieldnames=nazwy_pol)
#     writer.writeheader()  # Zapisz nagłówki kolumn
#     writer.writerows(dane)  # Zapisz dane