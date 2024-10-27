from faker import Faker
import csv
from datetime import date, timedelta
import random
fake = Faker("pl_PL")

# ilosc_numerow = 1000  # Liczba unikalnych numerów
# zakres = range(100000000, 999999999)
# # Generowanie unikalnych 9-cyfrowych numerów
# unikalne_numery = random.sample(zakres, ilosc_numerow)

dane_pacjenci=[]
#Pacjenci
with open("dane_pacjenci.csv", mode="w", newline="") as pacjenci_csv:
    writer = csv.writer(pacjenci_csv)

    for i in range(100):
        ID_pacjenta = fake.unique.random_int(100000000, 999999999)
        imie = fake.first_name()
        nazwisko = fake.last_name()
        nr_telefonu = fake.phone_number()
        miejscowosc = fake.city()
        ulica_i_numer_domu = fake.street_address()
        pesel = fake.unique.random_int(10000000000, 99999999999)

        writer.writerow([ID_pacjenta, imie, nazwisko, nr_telefonu, miejscowosc, ulica_i_numer_domu, pesel])

dane_recepty=[]
#Recepty
with open("dane_recepty.csv", mode="w", newline="") as recepty_csv:
    writer = csv.writer(recepty_csv)

    for i in range(100):
        ID_recepty = fake.unique.random_int(100000000000000, 999999999999999)
        waznosc = fake.random_int(30, 180, 30)
        czy_wykupiona = fake.boolean()
        data_wystawienia = fake.date_between((date.today() - timedelta(days=180)), date.today())

        writer.writerow([ID_recepty, waznosc, czy_wykupiona, data_wystawienia])


# # Zapis do pliku CSV
# with open("dane.csv", mode="w", newline="") as plik_csv:
#     nazwy_pol = ["id", "nazwa", "cena"]
#     writer = csv.DictWriter(plik_csv, fieldnames=nazwy_pol)
#     writer.writeheader()  # Zapisz nagłówki kolumn
#     writer.writerows(dane)  # Zapisz dane